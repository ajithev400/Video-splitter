# Generated by Django 4.1.3 on 2022-11-12 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media_name', models.CharField(max_length=150)),
                ('video', models.FileField(blank=True, null=True, upload_to='media')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='VideoSegment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('segment_name', models.CharField(blank=True, max_length=150, null=True)),
                ('video_segment', models.FileField(blank=True, null=True, upload_to='media/segment')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.videos')),
            ],
        ),
    ]