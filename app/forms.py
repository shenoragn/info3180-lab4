from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from werkzeug.utils import secure_filename

class UploadForm(FlaskForm):
    upload = FileField('picture', validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png'], 'Only Image Files')])
    