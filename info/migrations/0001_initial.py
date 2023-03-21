# Generated by Django 4.0.3 on 2022-04-28 13:26

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Assign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='AttendanceRange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.CharField(max_length=100, primary_key='True', serialize=False)),
                ('section', models.CharField(max_length=100)),
                ('sem', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'classes',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.CharField(max_length=50, primary_key='True', serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('shortname', models.CharField(default='X', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('id', models.CharField(max_length=100, primary_key='True', serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('USN', models.CharField(max_length=100, primary_key='True', serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=50)),
                ('DOB', models.DateField(default='1998-01-01')),
                ('class_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='info.class')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=50)),
                ('DOB', models.DateField(default='1980-01-01')),
                ('dept', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='info.dept')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StudentCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.student')),
            ],
            options={
                'verbose_name_plural': 'Marks',
                'unique_together': {('student', 'course')},
            },
        ),
        migrations.AddField(
            model_name='course',
            name='dept',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.dept'),
        ),
        migrations.AddField(
            model_name='class',
            name='dept',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.dept'),
        ),
        migrations.CreateModel(
            name='AttendanceClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('status', models.IntegerField(default=0)),
                ('assign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.assign')),
            ],
            options={
                'verbose_name': 'Attendance',
                'verbose_name_plural': 'Attendance',
            },
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default='2018-10-23')),
                ('status', models.BooleanField(default='True')),
                ('attendanceclass', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='info.attendanceclass')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.student')),
            ],
        ),
        migrations.CreateModel(
            name='AssignTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.CharField(choices=[('8:10 - 9:10', '8:10 - 9:10'), ('9:10 - 10:10', '9:10 - 10:10'), ('10:25 - 11:25', '10:25 - 11:25'), ('11:25 - 12:25', '11:25 - 12:25'), ('12:45 - 01:45', '12:45 - 01:45'), ('01:45 - 02:45', '01:45 - 02:45')], default='11:00 - 11:50', max_length=50)),
                ('day', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday')], max_length=15)),
                ('assign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.assign')),
            ],
        ),
        migrations.AddField(
            model_name='assign',
            name='class_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.class'),
        ),
        migrations.AddField(
            model_name='assign',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.course'),
        ),
        migrations.AddField(
            model_name='assign',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.teacher'),
        ),
        migrations.CreateModel(
            name='MarksClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Internals 1', 'Internals 1'), ('Internals 2', 'Internals 2'), ('Viva', 'Viva'), ('Practicals', 'Practicals'), ('Termwork', 'Termwork'), ('End Semester', 'End Semester')], default='Internals 1', max_length=50)),
                ('status', models.BooleanField(default='False')),
                ('assign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.assign')),
            ],
            options={
                'unique_together': {('assign', 'name')},
            },
        ),
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Internals 1', 'Internals 1'), ('Internals 2', 'Internals 2'), ('Viva', 'Viva'), ('Practicals', 'Practicals'), ('Termwork', 'Termwork'), ('End Semester', 'End Semester')], default='Internals 1', max_length=50)),
                ('marks1', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('studentcourse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.studentcourse')),
            ],
            options={
                'unique_together': {('studentcourse', 'name')},
            },
        ),
        migrations.CreateModel(
            name='AttendanceTotal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.student')),
            ],
            options={
                'unique_together': {('student', 'course')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='assign',
            unique_together={('course', 'class_id', 'teacher')},
        ),
    ]
