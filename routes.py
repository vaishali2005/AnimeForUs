from flask import Flask,redirect,request,url_for,render_template,jsonify,json
from datetime import datetime,timedelta
from flask_login import login_required,current_user,login_user,logout_user
from models import User,db,login,WatchHistory,FollowingAnime,AnimeComments
#for uploading the user given pic
from werkzeug.utils import secure_filename
import os
from dotenv import load_dotenv
# from fetch_data import anime_data
from fetch_data import get_anime_by_genre,anime_data,popular_anime,top_anime,trending_anime,upcoming_anime,recent_anime,TV_series,movies,airing_anime,search_by_id,search_by_query

# Load .env first
load_dotenv()
app = Flask(__name__)
app.secret_key=os.getenv('SECRET_KEY')
print("App Secret:", app.secret_key)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///animeforusDB.db'

app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
#defining the path of  folder
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#EXTENSIONS TO ACCPET USER PROFILE PICS
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


db.init_app(app)

login.init_app(app)
login.login_view = 'login'

with app.app_context():
    db.create_all()
 

@app.route('/')
def index():
    # print(popular_anime())
    return render_template('index.html', trending_anime=trending_anime(),top_anime=top_anime(),popular_anime=popular_anime(),recent_anime=recent_anime())


#REGISTER
@app.route('/register',methods=['GET','POST'])
def register():
    try:
        if current_user.is_authenticated:
            return redirect('/')
        if request.method == 'POST':
            email = request.form.get('email')
            username = request.form.get('username')
            password = request.form.get('password')
            if User.query.filter_by(email=email).first():
                return "This Email is alredy exists"
            user = User(email=email,username=username)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            return redirect('/login')
        return render_template('register.html')
    except Exception as e:
        db.session.rollback()
        print(e)
        return "Coulnt register new candidate"

#LOGIN
@app.route('/login', methods = ['GET','POST'])
def login():
    try:
        if current_user.is_authenticated:
            return redirect('/')
        if request.method == 'POST':
            email = request.form.get('email')
            # password = request.form.get('password')
            user = User.query.filter_by(email=email).first()
            # print(user,user.check_password(request.form.get('password')))
            if user is not None and user.check_password(request.form.get('password')):
                login_user(user)
                return redirect('/') 
            return render_template('register.html')
        return render_template('login.html')
    except Exception as e:
        db.session.rollback()
        print(e)
        return "Couldn't logged in"

#LOGOUT
@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')

#PROFILE
@app.route('/profile')
@login_required
def profile():
    user_id = current_user.id
    watching_list = WatchHistory.query.filter_by(user_id = user_id).all()
    favrouit_anime = FollowingAnime.query.filter_by(user_id = user_id).all()
    return render_template('profile.html',watching_list=watching_list,fav_animes = favrouit_anime)

@app.route('/update_profile/<string:email>',methods=['POST','GET'] )
@login_required
def update_profile(email):
    try:
        if request.method=='POST':
            user = User.query.filter_by(email=email).first() 
            # print(user)
            user.username = request.form.get('username')
            chng_password = request.form.get('chng_password')
            # print(user,chng_password)
            if chng_password is not None:
                user.set_password(chng_password)
            db.session.commit()
            return redirect('/')
        return render_template('profile.html')
    except Exception as e:
        db.session.rollback()
        print(e)
        return "Changes couldn't save"

@app.route('/update_profile_pic/<string:email>', methods = ['POST','GET'])
@login_required
def update_profile_pic(email):
    try:
        if request.method == 'POST':
            user = User.query.filter_by(email=email).first()
            print(user)
            
            file = request.files.get('profile_pic')
            # print(request.files)
            
            if file and file.filename != " " and allowed_file(file.filename):
                #secure filename
                filename = secure_filename(file.filename)
                
                #make file unique with unique name
                unique_name = str(user.id)+"_"+filename
                filepath = os.path.join(app.config['UPLOAD_FOLDER'],unique_name)
                file.save(filepath)
                
                #delete old file
                if user.profile_pic != 'default.jpg':
                    old_path = os.path.join(app.config['UPLOAD_FOLDER'],user.profile_pic)
                    if os.path.exists(old_path):
                        os.remove(old_path)
                                        
                #save new pic in DB
                user.profile_pic = unique_name
                db.session.commit()
                print('done')
                return redirect('/')
        return render_template('profile.html')
    except Exception as e:
        db.session.rollback()
        print(e)
        return "couldnt Upload new profile pic"
    
@app.route('/categories')
def categories():
    return render_template('categories-main.html')

@app.route('/genre/<int:id>/<string:name>')
def genre(id,name):
    anime_list = get_anime_by_genre(id)
    return render_template('category.html',anime_list=anime_list,name = name)
    
all_category={
    'Top': top_anime(),
    'Popular':popular_anime(),
    'Trending':trending_anime(),
    'Recent':recent_anime(),
    'Upcoming':upcoming_anime(),
    'Airing':airing_anime(),
    'Movies':movies(),
    'TV Series':TV_series()
}
@app.route('/category/<string:name>')
def category(name):
    category_name = all_category.get(name)
    if not category_name:
        return "Invalid Category"
    return render_template('category.html',anime_list=category_name,name=name)

@app.template_filter('format_views')
def format_views(value):
    if value >= 1_000_000:
        return f"{value/1_000_000:.1f}M"
    elif value >= 1_000:
        return f"{value/1_000:.1f}K"
    return value       
    
@app.template_filter('timeago')
def timeago(dt):
    now = datetime.utcnow()
    diff = now - dt
    seconds = diff.total_seconds()

    if seconds < 60:
        return f"{int(seconds)} sec ago"
    elif seconds < 3600:
        return f"{int(seconds // 60)} min ago"
    elif seconds < 86400:
        return f"{int(seconds // 3600)} hr ago"
    else:
        return f"{int(seconds // 86400)} days ago"    
    
@app.route('/anime_details/<int:anime_id>')
def anime_details(anime_id):
    search_anime = search_by_id(anime_id)
    find_genre = search_anime['genres'][0]['mal_id']
    # user_id = current_user.id
    comment=[]
    comment = AnimeComments.query.filter_by(anime_id=anime_id).all()
    # print(search_anime['genres'][0]['name'])
    genre = get_anime_by_genre(find_genre)
    return render_template('anime-details.html',anime = search_anime,genre=genre,comment=comment)

@login_required
@app.route('/anime_watching/<int:anime_id>/', defaults={'ep': None})
@app.route('/anime_watching/<int:anime_id>/<int:ep>')
def anime_watching(anime_id,ep):
    user_id = current_user.id
    search_anime = search_by_id(anime_id)
    if search_anime['title_english']:
        anime_name = search_anime['title_english']
    else:
        anime_name = search_anime['title']
    img_url = search_anime['images']['jpg']['large_image_url']
    anime_type = search_anime['type']
    # id = WatchHistory.query.filter_by(id = anime_id).first()
    # print(id,user_id,anime_id)
    comment=[]
    try:
        comment = AnimeComments.query.filter_by(anime_id=anime_id).all()
        # print(comment)
        # if WatchHistory.query.filter_by(anime_id = anime_id).first() and WatchHistory.query.filter_by(user_id=user_id).first():
        #     return render_template('anime-watching.html',anime =  search_anime)
        record=WatchHistory.query.filter_by(anime_id = anime_id,user_id=user_id).first()
        if ep is None:
            if record:
                ep = record.episode  
            else:
                ep = 1
        if record:
            record.episode=ep
            db.session.commit()   
            return render_template('anime-watching.html',current_episode=ep,anime=search_anime,comment=comment)
  
        if FollowingAnime.query.filter_by(anime_id=anime_id).first() and FollowingAnime.query.filter_by(user_id=user_id).first():
            remove_anime(anime_id, user_id,1) 
        watch = WatchHistory(anime_id=anime_id,user_id=user_id,anime_name = anime_name,img_url=img_url,anime_type=anime_type) 
        db.session.add(watch)
        db.session.commit()   
    except Exception as e:
        db.session.rollback()
        print(e)
    return render_template('anime-watching.html',anime =  search_anime,current_episode=ep,comment=comment)

# @login_required
# @app.route('/watch_ep/<int:anime_id>/', defaults={'ep': None})
# @app.route('/watch_ep/<int:anime_id>/<int:ep>')
# def watch_ep(anime_id,ep):
#     user_id = current_user.id
#     anime = search_by_id(anime_id)
#     try:
#         record=WatchHistory.query.filter_by(anime_id = anime_id,user_id=user_id).first()
#         if ep is None:
#             if record:
#                 ep = record.episode   # 🔥 load from DB
#             else:
#                 ep = 1   # default
#         if record:
#             record.episode=ep 
#             db.session.commit()
            
#         else:
#             return('/')
#     except Exception as e:
#         db.session.rollback()
#         print(e)    
#     return render_template('anime-watching.html',current_episode=ep,anime=anime)
@login_required
@app.route('/fav_anime/<int:anime_id>')
def fav_anime(anime_id):
    search_anime = search_by_id(anime_id)
    user_id = current_user.id
    if search_anime['title_english']:
        anime_name = search_anime['title_english']
    else:
        anime_name = search_anime['title']
    img_url = search_anime['images']['jpg']['large_image_url']
    episode = search_anime['episodes']
    try:
        if FollowingAnime.query.filter_by(anime_id = anime_id).first() and FollowingAnime.query.filter_by(user_id=user_id).first():
            return redirect('/anime_details',anime_id=anime_id)
        watch = FollowingAnime(anime_id = anime_id,user_id=user_id,anime_name=anime_name,img_url=img_url,episode=episode)
        print(watch)
        db.session.add(watch)
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
    return redirect(request.referrer)

@login_required
@app.route('/remove_anime/<int:anime_id>/<int:data>')
def remove_anime(anime_id,data):
    user_id = current_user.id
    try:
        if data == 1:
            if FollowingAnime.query.filter_by(anime_id = anime_id).first() and FollowingAnime.query.filter_by(user_id = user_id).first():
                FollowingAnime.query.filter_by(anime_id = anime_id).delete()
        elif data == 0:
            if WatchHistory.query.filter_by(anime_id = anime_id).first() and WatchHistory.query.filter_by(user_id=user_id).first():
               WatchHistory.query.filter_by(anime_id = anime_id).delete()
        db.session.commit()
        return redirect(request.referrer)
    except Exception as e:
        print(e)
        db.session.rollback()
    return "couldn't delete record"


@app.route('/search_anime')
def search_anime():
    search_item = request.args.get('search_item')
    # print(search_item)
    anime = search_by_query(search_item)
    # print(anime)
    return render_template('search-anime.html',anime=anime,item=search_item)


@app.route('/anime_comments/<int:anime_id>/',methods=['GET','POST'])
@login_required
def anime_commnets(anime_id):
    try:
        if request.method=='POST':
            anime_id = anime_id
            new_comment = request.form.get('comment')
            user_id = current_user.id
            username = current_user.username
            user_img = current_user.profile_pic or "default.jpg"
            old_comment= AnimeComments.query.filter_by(anime_id = anime_id,user_id=user_id).first()
            if old_comment :
                old_comment.comment = new_comment
                old_comment.time = datetime.utcnow()
            else:
                add_comment = AnimeComments(anime_id = anime_id,user_id=user_id,username=username,comment=new_comment,img_url=user_img)
                db.session.add(add_comment)
            db.session.commit()
            return redirect(request.referrer)
        else:
            return "Hello" 
    except Exception as e:
        db.session.rollback()
        print(e)




#EXTRA
# @app.route('/move_to_watch/<int:anime_id>/<int:user_id>')
# def move_to_watch(anime_id,user_id):
#     try:
#         if FollowingAnime.query.filter_by(anime_id = anime_id).first() and FollowingAnime.query.filter_by(user_id = user_id).first():
#             # remove_anime(anime_id, user_id,1)
#             search_anime = search_by_id(anime_id)
#             if search_anime['title_english']:
#                 anime_name = search_anime['title_english']
#             else:
#                 anime_name = search_anime['title']
#             img_url = search_anime['images']['jpg']['large_image_url']
#             anime_type = search_anime['type']
#             watch = WatchHistory(anime_id=anime_id,user_id=user_id,anime_name = anime_name,img_url=img_url,anime_type=anime_type) 
#             db.session.add(watch)
#             db.session.commit() 
#             remove_anime(anime_id, user_id,1) 
#             return render_template('anime-watching.html',anime =  search_anime)
#         return 'could not move'
            
#     except Exception as e:
#         print(e)
#         db.session.rollback()


if __name__=='__main__':
    app.run(debug=True)