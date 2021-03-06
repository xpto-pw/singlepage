# Generated by Django 3.2.5 on 2021-07-27 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacto',
            name='id',
        ),
        migrations.RemoveField(
            model_name='jogador',
            name='author',
        ),
        migrations.RemoveField(
            model_name='jogador',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='jogador',
            name='cor1',
        ),
        migrations.RemoveField(
            model_name='jogador',
            name='cor2',
        ),
        migrations.RemoveField(
            model_name='jogador',
            name='cor3',
        ),
        migrations.RemoveField(
            model_name='jogador',
            name='cor4',
        ),
        migrations.AddField(
            model_name='contacto',
            name='username',
            field=models.CharField(default='Unspecified', max_length=30, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AddField(
            model_name='jogador',
            name='apelido',
            field=models.CharField(default='Unspecified', max_length=15),
        ),
        migrations.AddField(
            model_name='jogador',
            name='clube',
            field=models.CharField(default='Unspecified', max_length=50),
        ),
        migrations.AddField(
            model_name='jogador',
            name='contacto',
            field=models.ForeignKey(default='Unspecified', on_delete=django.db.models.deletion.CASCADE, to='website.contacto'),
        ),
        migrations.AddField(
            model_name='jogador',
            name='nome',
            field=models.CharField(default='Unspecified', max_length=15),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='apelido',
            field=models.CharField(default='Unspecified', max_length=30),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='email',
            field=models.CharField(default='Unspecified', max_length=30),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='nome',
            field=models.CharField(default='Unspecified', max_length=30),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='telefone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='jogador',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
    ]
