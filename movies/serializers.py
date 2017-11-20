from .models import Movie, Person, Role
from rest_framework import serializers


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ("id", "name")


class RoleSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField(source='person.id')
    name = serializers.ReadOnlyField(source='person.name')

    class Meta:
        model = Role
        fields = ("id", "name", "role",)


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    actors = RoleSerializer(source='role_set', many=True)
    # actors = serializers.HyperlinkedRelatedField(
    # view_name='api:person-detail', read_only=True)

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "director", "actors", "year")
        # extra_kwargs = {
        #     'url': {'view_name': 'person'},
        #     'director': {'view_name': 'person'},
        #     'lookup
        # }
