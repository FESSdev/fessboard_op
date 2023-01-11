# Generated by Django 4.1.5 on 2023-01-11 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GroupsInProjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'groups_in_projects',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ManagersInEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'managers_in_Event',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ManagersInProjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'managers_in_projects',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ParticipantsInEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'participants_in_Event',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProjectFields',
            fields=[
                ('field_id', models.AutoField(primary_key=True, serialize=False)),
                ('field', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'project_fields',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProjectGrades',
            fields=[
                ('grade_id', models.AutoField(primary_key=True, serialize=False)),
                ('grade', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'project_grades',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('project_id', models.AutoField(primary_key=True, serialize=False)),
                ('project_name', models.CharField(max_length=255)),
                ('project_description', models.TextField()),
                ('project_result', models.TextField()),
                ('is_frozen', models.IntegerField()),
                ('project_start_date', models.DateField()),
                ('project_end_date', models.DateField()),
                ('project_dateadded', models.DateTimeField(blank=True, db_column='project_dateAdded', null=True)),
                ('project_dateupdated', models.DateTimeField(blank=True, db_column='project_dateUpdated', null=True)),
            ],
            options={
                'db_table': 'projects',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Regions',
            fields=[
                ('region_id', models.AutoField(primary_key=True, serialize=False)),
                ('region', models.CharField(max_length=255)),
                ('is_foreign', models.IntegerField()),
            ],
            options={
                'db_table': 'regions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('student_id', models.AutoField(primary_key=True, serialize=False)),
                ('student_surname', models.CharField(max_length=255)),
                ('student_name', models.CharField(max_length=255)),
                ('student_midname', models.CharField(max_length=255)),
                ('bachelors_start_year', models.TextField(blank=True, null=True)),
                ('masters_start_year', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'students',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StudentsInGroups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'students_in_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StudentStatuses',
            fields=[
                ('student_status_id', models.AutoField(primary_key=True, serialize=False)),
                ('student_status', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'student_statuses',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('teacher_id', models.AutoField(primary_key=True, serialize=False)),
                ('teacher_surname', models.CharField(max_length=255)),
                ('teacher_name', models.CharField(max_length=255)),
                ('teacher_midname', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'teachers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TeachersInEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'teachers_in_Event',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TeachersInProjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'teachers_in_projects',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Universities',
            fields=[
                ('university_id', models.AutoField(primary_key=True, serialize=False)),
                ('university_name', models.CharField(max_length=255)),
                ('university_logo', models.TextField()),
            ],
            options={
                'db_table': 'universities',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='???')),
                ('start_date', models.DateField(verbose_name='???')),
                ('end_date', models.DateField(verbose_name='???')),
                ('description', models.TextField(verbose_name='???')),
                ('is_frozen', models.IntegerField(verbose_name='???')),
            ],
        ),
        migrations.CreateModel(
            name='FieldSphere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='???')),
            ],
        ),
        migrations.CreateModel(
            name='Sphere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='???')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='???')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='???')),
                ('website', models.TextField(verbose_name='???')),
                ('sphere', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='homepage.sphere', verbose_name='???')),
                ('type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='homepage.type', verbose_name='???')),
            ],
        ),
    ]
