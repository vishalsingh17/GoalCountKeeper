from rest_framework import serializers
from .models import PlayerTable, ChildTable

class ChildTableSerializer(serializers.ModelSerializer):
	# x= ChildTable.objects.all().values
	class Meta:
		model = ChildTable
		fields = ('season','goals','fk')
		# fields =('fk',)

class PlayerTableSerializer(serializers.ModelSerializer):
    childtable_set = ChildTableSerializer(many=True, read_only=True)
    
    class Meta:
        model = PlayerTable
        fields =  ('childtable_set','player_name','player_id')
	# def get_related_field(self, model_field):
 #            # Handles initializing the `subcategories` field
 #            return PlayerTableSerializer()


