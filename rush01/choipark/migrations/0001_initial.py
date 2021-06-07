from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('content', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('downvotes', models.ManyToManyField(related_name='downvotes_article', to=settings.AUTH_USER_MODEL)),
                ('upvotes', models.ManyToManyField(related_name='upvotes_article', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='name')),
                ('surname', models.CharField(max_length=30, verbose_name='surname')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('profile_image', models.ImageField(blank=True, upload_to='', verbose_name='profile_image')),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CommentsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='choipark.articlemodel')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('downvotes', models.ManyToManyField(related_name='downvotes_comment', to=settings.AUTH_USER_MODEL)),
                ('reply', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='choipark.commentsmodel')),
                ('upvotes', models.ManyToManyField(related_name='upvotes_comment', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
