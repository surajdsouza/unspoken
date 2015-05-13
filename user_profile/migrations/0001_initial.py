# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.BinaryField()),
                ('upvote', models.IntegerField(default=0)),
                ('downvote', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(default=b'NA', max_length=2, choices=[(b'F', b'Friend'), (b'FO', b'Foe'), (b'B', b'Blocked'), (b'NA', b'Not Accepted')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(unique=True, max_length=100)),
                ('f_name', models.CharField(max_length=100)),
                ('m_name', models.CharField(max_length=100)),
                ('l_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(default=None, max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female'), (b'O', b'Other'), (None, b'')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='contact',
            name='contact',
            field=models.ForeignKey(related_name=b'contact', to='user_profile.Profile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contact',
            name='user',
            field=models.ForeignKey(related_name=b'users_contact', to='user_profile.Profile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='commenter',
            field=models.ForeignKey(related_name=b'commenter', to='user_profile.Profile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(related_name=b'parent_comment', to='user_profile.Comment', db_constraint=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(related_name=b'op', to='user_profile.Profile'),
            preserve_default=True,
        ),
    ]
