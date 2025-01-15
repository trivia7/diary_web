from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Daftar diary yang akan ditampilkan
diaries = []

# Halaman utama
@app.route('/')
def index():
    return render_template('index.html', diaries=diaries)

# Halaman untuk menulis diary baru
@app.route('/new', methods=['GET', 'POST'])
def new_diary():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        diaries.append({'title': title, 'content': content, 'comments': []})
        return redirect(url_for('index'))
    return render_template('diary.html')

# Halaman untuk melihat diary dan menambahkan komentar
@app.route('/diary/<int:diary_id>', methods=['GET', 'POST'])
def view_diary(diary_id):
    diary = diaries[diary_id]
    if request.method == 'POST':
        comment = request.form['comment']
        diary['comments'].append(comment)
    return render_template('diary.html', diary=diary, diary_id=diary_id)

if __name__ == '__main__':
    app.run(debug=True)
