# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0001_initial'),
        ('albums', '0001_initial'),
        ('tracks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='album',
            field=models.ForeignKey(default=None, to='albums.Album'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='track',
            name='artist',
            field=models.ForeignKey(default=None, to='artists.Artist'),
            preserve_default=False,
        ),
    ]
