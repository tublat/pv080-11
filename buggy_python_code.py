# contains bunch of buggy examples
# taken from https://hackernoon.com/10-common-security-gotchas-in-python-and-how-to-avoid-them-e19fbe265e03
import subprocess
import base64
import flask


def transcode_file(filename):
    command = 'ffmpeg -i "{source}" output_file.mpg'.format(source=filename)
    subprocess.call(command, shell=True)  # a bad idea!


def checker(user):
    assert user.is_admin, 'user does not have access'
    # secure code...


class RunBinSh:
    def __reduce__(self):
        return (subprocess.Popen, (('/bin/sh',),))


def import_urlib_version(version):
    exec("import urllib%s as urllib" % version)


@app.route('/')
def index():
    module = flask.request.args.get("module")
    import_urlib_version(module)


print(base64.b64encode(pickle.dumps(RunBinSh())))
