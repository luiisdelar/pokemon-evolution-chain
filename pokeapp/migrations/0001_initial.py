# Generated by Django 3.2.7 on 2021-09-16 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EvolsTo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evols_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pokeapp.evolsto')),
            ],
        ),
        migrations.CreateModel(
            name='EvolutionChain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evolutions', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pokeapp.evolsto')),
            ],
        ),
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hp', models.IntegerField()),
                ('attack', models.IntegerField()),
                ('defense', models.IntegerField()),
                ('special_attack', models.IntegerField()),
                ('special_defense', models.IntegerField()),
                ('speed', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iid', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('evolution_chain', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pokeapp.evolutionchain')),
                ('stats', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pokeapp.stats')),
            ],
        ),
        migrations.AddField(
            model_name='evolsto',
            name='pokemon',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pokeapp.pokemon'),
        ),
    ]
