from flask import Flask, render_template, redirect, url_for, request
from flask import flash
from werkzeug.security import generate_password_hash, check_password_hash
import DynamoDB as db
import S3

app = Flask(__name__)
ALLOWED_EXTENSIONS = ['png', 'jpg', 'JPG', 'PNG']
app.secret_key = 'Happy Wind Man'
bucket_name='ece1779avatarss'


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        user_name = request.form['user_name']
        password = request.form['password']
        if user_name == "":
            flash("Please enter your username")
            return redirect(url_for('login_page'))
        else:
            if password == "":
                flash("Please enter your password")
                return redirect(url_for('login_page'))
            else:
                if db.scan_table('user_name', 'S', user_name)[1] == 0:
                    flash("User name doesn't exist")
                    return redirect(url_for('login_page'))
                else:
                    if not check_password_hash(db.get_item('People', 'user_name', user_name, "password", "S"),
                                               password):
                        flash("Wrong password")
                        return redirect(url_for('login_page'))
                    elif check_password_hash(db.get_item('People', 'user_name', user_name, "password", "S"), password):
                        return redirect(url_for('private_page', user_name=user_name))
                    else:
                        flash("Unknown errors")
                        return redirect(url_for('login_page'))
    else:
        flash("Hello")
        return render_template("Login_Page.html")


@app.route('/logout/<user_name>', methods=['GET', 'POST'])
def logout_page(user_name):
    avatar_address = 'https://s3.amazonaws.com/'+ bucket_name + '/People/' + str(user_name) + '.jpg'
    flash("Successfully logged out of your page!")
    return render_template("Logout_Page.html", user_name=user_name, avatar_address=avatar_address)


@app.route('/register_page', methods=['GET', 'POST'])
def register_page():
    if request.method == 'POST':
        user_name = request.form['user_name']
        password = request.form['password']
        password_confirm = request.form['password_confirm']
        if user_name == "":
            flash("Please enter your username ", "ok")
            return redirect(url_for('register_page'))
        else:
            if password == "":
                flash("Please enter your password", "ok")
                return redirect(url_for('register_page'))
            else:
                if password_confirm == "":
                    flash("Please confirm your password", "ok")
                    return redirect(url_for('register_page'))
                else:
                    if db.scan_table('name', 'S', user_name)[1] == 0:
                        if password == password_confirm:
                            password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
                            S3.copy_photo(user_name)
                            default_memo = str("This is your private page " + user_name + " ,please enjoy!")
                            db.put_item_list(table_name='People', key_name='user_name', key_value=user_name,
                                             attribute='password', attribute_type='S', attribute_value=password,)
                            # Save all the contents to Memo table
                            db.put_item_list(table_name='Memo', key_name='user_name', key_value=user_name,
                                             attribute='memo', attribute_type='S',
                                             attribute_value=default_memo)
                            # Setup the Private table
                            db.put_item_list(table_name='Private', key_name='user_name', key_value=user_name,
                                             attribute='Private', attribute_type='L',
                                             attribute_value=[])
                            flash('New account created successfully!', "ok")
                            return redirect(url_for('login_page'))
                        else:
                            flash('The password confirmation not pass!', "ok")
                            return redirect(url_for('register_page'))
                    else:
                        flash('The user name already existed!', "ok")
                        return redirect(url_for('register_page'))
    else:
        return render_template("Register_Page.html")


@app.route('/private/setting/<user_name>', methods=['GET', 'POST'])
def private_setting_page(user_name):
    avatar_address = 'https://s3.amazonaws.com/'+ bucket_name + '/People/' + str(user_name) + '.jpg'
    return render_template("Private_Setting_Page.html", user_name=user_name, avatar_address=avatar_address)


@app.route('/text_change/<user_name>', methods=['GET', 'POST'])
def text_change(user_name):
    avatar_address = 'https://s3.amazonaws.com/ece1779avatar/People/' + str(user_name) + '.jpg'
    old_password = request.form['old_password']
    new_password = request.form['new_password']
    password_confirmation = request.form['password_confirm']
    if request.method == 'POST':
        if old_password == "":
            flash("Please enter your old passwords", "one")
            return redirect(url_for('private_setting_page', user_name=user_name))
        else:
            if new_password == "":
                flash("Please enter your new passwords", "one")
                return redirect(url_for('private_setting_page', user_name=user_name))
            else:
                if password_confirmation == "":
                    flash("Please confirm your new passwords", "one")
                    return redirect(url_for('private_setting_page', user_name=user_name))
                else:
                    if not check_password_hash(db.get_item('People', 'user_name', user_name, "password", "S"),
                                               old_password):
                        flash("Your old password is invalid, please type in again!", "one")
                        return redirect(url_for('private_setting_page', user_name=user_name))
                    else:
                        if new_password != password_confirmation:
                            flash("Your new password typed in second does not match the first time, please type in again!", "one")
                            return redirect(url_for('private_setting_page', user_name=user_name))
                        elif new_password == password_confirmation:
                            flash(
                                "Your new password is successfully changed!","one")
                            db.put_item_list(table_name='People', key_name='user_name', key_value=user_name, attribute='password', attribute_type='S',
                                        attribute_value=generate_password_hash(new_password, method='pbkdf2:sha256', salt_length=8))
                            return redirect(url_for('private_setting_page', user_name=user_name))
                            # Unknown error
                        else:
                            flash("Unknown errors")
                            return redirect(url_for('private_setting_page', user_name=user_name))
    return render_template("Private_Setting_Page.html", user_name=user_name, avatar_address=avatar_address)


@app.route('/image_change/<user_name>', methods=['GET', 'POST'])
def image_change(user_name):
    avatar_address = 'https://s3.amazonaws.com/'+ bucket_name + '/People/' + str(user_name) + '.jpg'
    if request.method == 'POST':
        file_avatar = request.files["file_av"]
        if request.method == 'POST':
            if not (file_avatar or allowed_file(file_avatar.filename)):
                flash("Your avatar is invalid, please try again!", "two")
                return redirect(url_for('private_setting_page', user_name=user_name))
            elif file_avatar or allowed_file(file_avatar.filename):
                S3.upload_photo(user_name, file_avatar)
                return redirect(url_for('private_setting_page', user_name=user_name))
            else:
                flash("Unknown errors", "two")
                return redirect(url_for('private_setting_page', user_name=user_name))
    return render_template("Private_Setting_Page.html", user_name=user_name, avatar_address=avatar_address)


@app.route('/memo_change/<user_name>', methods=['GET', 'POST'])
def memo_change(user_name):
    avatar_address = 'https://s3.amazonaws.com/'+ bucket_name + '/People/' + str(user_name) + '.jpg'
    if request.method == 'POST':
        memo = request.form["memo"]
        if request.method == 'POST':
            if memo == "":
                flash("please enter your memo", "three")
                return redirect(url_for('private_setting_page', user_name=user_name, avatar_address=avatar_address))
            else:
                if memo != "":
                    flash("memo uploaded successfully!", "three")
                    db.put_item_list(table_name='Memo', key_name='user_name', key_value=user_name, attribute='memo',
                                     attribute_type='S', attribute_value=memo)
                    return redirect(url_for('private_setting_page', user_name=user_name))
                else:
                    flash("Unknown errors", "three")
                    return redirect(url_for('private_setting_page', user_name=user_name))
    return render_template("Private_Setting_Page.html", user_name=user_name, avatar_address=avatar_address)


@app.route('/alluser/<user_name>', methods=['GET', 'POST'])
def private_all_user_page(user_name):
    avatar_address = 'https://s3.amazonaws.com/'+ bucket_name + '/People/' + str(user_name) + '.jpg'
    messages = db.get_all_items(table_name="People", attribute_name="user_name")
    memo_list = []
    avatar_list = []
    for name_memo in messages:
        memo_list.append(db.get_item('Memo', 'user_name', name_memo, "memo", "S"))
        avatar_list.append('https://s3.amazonaws.com/'+ bucket_name + '/People/' + str(name_memo) + '.jpg')
    return render_template("Private_User_Page.html", user_name=user_name, messages=messages, memo_list=memo_list,
                           avatar_list=avatar_list, avatar_address=avatar_address)


@app.route('/private/<user_name>', methods=['GET', 'POST'])
def private_page(user_name):
    avatar_address = 'https://s3.amazonaws.com/'+ bucket_name + '/People/' + str(user_name) + '.jpg'
    memo = db.get_item(table_name='Memo', key_name='user_name', key_value=user_name, attribute='memo', attribute_type='S')
    messages = db.get_item(table_name='Private', key_name='user_name', key_value=user_name, attribute='Private', attribute_type='L')
    if request.method == 'POST':
        private_message = request.form['private_message']
        private_receiver = request.form['private_receiver']
        private_sender = str(user_name)
        item = []
        if private_message == "":
            flash("Please enter your message!")
            return redirect(url_for('private_page', user_name=user_name))
        else:
            if private_receiver == "":
                flash("Please enter one valid receiver!")
                return redirect(url_for('private_page', user_name=user_name))
            else:
                if db.scan_table('user_name', 'S', private_receiver)[1] == 0:
                    flash("The receiver's name does not exist!")
                    return redirect(url_for('private_page', user_name=user_name))
                elif private_message != "" and private_receiver != "" \
                        and db.scan_table('user_name', 'S', private_receiver)[1] != 0:
                    private_sender_item = "1." + private_sender
                    item.append(private_sender_item)
                    avatar_address_item = "2." + avatar_address
                    item.append(avatar_address_item)
                    private_message_item = "3." + private_message
                    item.append(private_message_item)
                    add_item = {'SS': item}
                    messages.append(add_item)
                    db.put_item_list(table_name='Private', key_name='user_name', key_value=str(private_receiver),
                                     attribute='Private', attribute_type='L', attribute_value=messages)
                    flash("Message successfully sent! You could try to send another one")
                    return redirect(url_for('private_page', user_name=user_name))
                else:
                    flash("Unknown error")
                    return redirect(url_for('private_page', user_name=user_name))

    else:
        return render_template("Private_Page.html", user_name=user_name, messages=messages, memo=memo,
                               avatar_address=avatar_address)


@app.route('/public/<user_name>', methods=['GET', 'POST'])
def public_page(user_name):
    avatar_address = 'https://s3.amazonaws.com/'+ bucket_name + '/People/' + str(user_name) + '.jpg'
    messages = db.get_item(table_name='Public', key_name='user_name', key_value='public',attribute='messages', attribute_type='L')
    print(messages)
    if request.method == 'POST':
        public_message = request.form['public_message']
        sender_name = str(user_name)
        item = []
        if public_message == "":
            flash("Please enter your message!")
            return redirect(url_for('public_page', user_name=user_name))
        elif public_message != "":
            # append sender's name to the list
            sender_name_item = str("1." + sender_name)
            item.append(sender_name_item)
            avatar_address_items = str("2." + avatar_address)
            item.append(avatar_address_items)
            public_message_item = str("3." + public_message)
            item.append(public_message_item)
            add_item = {'SS': item  }
            messages.append(add_item)
            print(messages)
            db.put_item_list(table_name='Public', key_name='user_name', key_value='public',
                             attribute='messages', attribute_type='L', attribute_value=messages)
            flash("Your message is successfully posted on the public page!")
            return redirect(url_for('public_page', user_name=user_name))
        else:
            flash("Unknown error!")
            return redirect(url_for('public_page', user_name=user_name))
    else:
        return render_template("Public_Page.html", user_name=user_name, avatar_address=avatar_address, messages=messages)


if __name__ == '__main__':
    app.run()
