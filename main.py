from flask import Flask, render_template

app = Flask(__name__)


def main():
    app.run()


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def get_rating_result(nickname, level, rating):
    return render_template(
        'index.html',
        nickname=nickname,
        level=level,
        rating=rating,
    )


if __name__ == '__main__':
    main()
