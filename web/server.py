from flask import Flask, make_response, render_template, request

from form import MovesForm
from tools import decide, get_time, random_filename

app = Flask(__name__)
app.secret_key = 'very secret key'


def foo(form):
    def bar(x, y):
        return getattr(form, 'move_{}_{}'.format(x, y))(maxlength=2)

    return bar


@app.route('/', methods=['GET', 'POST'])
def index():
    form = MovesForm(request.form)
    fields = {'form': form, 'ts': get_time()}
    resp = make_response(render_template('index.html', **fields))
    filename = request.cookies.get('file')

    print(request.remote_addr, filename)
    if filename is None:
        filename = random_filename()
        resp.set_cookie('file', filename)
        # return resp

    filename = 'static/generated/' + filename

    if request.method == 'POST' and form.validate():
        data = form.data
        ff_type = data.pop('ff_type')
        decide(data, ff_type, filename)

    return resp


@app.route('/form')
def wtf_form():
    form = MovesForm(request.form)
    return render_template('form.html', form=form,
                           foo=foo(form))


@app.route('/file.<ext>')
def get_file(ext):
    print(ext)
    file = 'generated/{}.{}'.format(request.cookies.get('file'), ext)
    return app.send_static_file(file)


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        debug=True
    )
