# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-22 21:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
                ('width', models.FloatField()),
                ('height', models.FloatField()),
                ('remote', models.CharField(blank=True, default='', max_length=600, null=True)),
                ('newtab', models.BooleanField(default=False)),
                ('transition', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(blank=True, default='', help_text='this is the URL you want for your page, leading / is implied, empty string means homepage', max_length=300, null=True, unique=True, verbose_name='URL')),
                ('page_title', models.CharField(blank=True, default='relief z\xe9ro', help_text="title of the page, example : 'Home'", max_length=300, null=True, verbose_name='Page title')),
                ('page_background', models.CharField(default='#ffffff', help_text='set custom background color', max_length=7, verbose_name='Background color')),
                ('seo_block', models.BooleanField(default=False, help_text='disallow robots, like GoogleBot, for page indexing', verbose_name='Block webcrawlers')),
                ('seo_description', models.TextField(blank=True, default='', help_text='description metatag, should be picked by crawlers for web browsers results (no guarantee, actual text content might overrule this)', null=True, verbose_name='Page description')),
                ('image', models.ImageField(help_text='the lighter the better, 300ko or less is recommended. Submit the image to get a preview for links below', upload_to='pages/', verbose_name='Image')),
                ('height_zoom', models.FloatField(default=100.0, help_text='height (in percents) of drawing area, 100 (default) means all browser area, no scroll', verbose_name='Image zoom - height')),
                ('width_zoom', models.FloatField(default=100.0, help_text='width (in percents) of drawing area, 100 (default) means all browser area, no scroll', verbose_name='Image zoom - width')),
                ('smooth_loading', models.BooleanField(default=False, help_text='when enabled page will fade-in only when fully loaded, this is not recommended for heavy images', verbose_name='Smooth loading')),
                ('meta_width', models.IntegerField(default=0, verbose_name='Image width (px)')),
                ('meta_height', models.IntegerField(default=0, verbose_name='Image height (px)')),
                ('meta_size', models.IntegerField(default=0, verbose_name='Image size (bytes)')),
            ],
            options={
                'ordering': ['url'],
            },
        ),
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=120, unique=True)),
                ('cssString', models.TextField(default='')),
            ],
        ),
        migrations.AddField(
            model_name='link',
            name='hoverStyle',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='end_links', to='web.Style'),
        ),
        migrations.AddField(
            model_name='link',
            name='initStyle',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='init_links', to='web.Style'),
        ),
        migrations.AddField(
            model_name='link',
            name='page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='froms', to='web.Page'),
        ),
        migrations.AddField(
            model_name='link',
            name='target',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='links', to='web.Page'),
        ),
    ]
