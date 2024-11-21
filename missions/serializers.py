from rest_framework import serializers

from missions.models import Mission, Target


class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = ["id", "name", "country", "notes", "is_complete"]

    def validate(self, data):
        if "notes" in data and data.get("is_complete"):
            raise serializers.ValidationError("Cannot update notes for a completed target.")
        return data


class MissionSerializer(serializers.ModelSerializer):
    targets = serializers.PrimaryKeyRelatedField(queryset=Target.objects.all(), many=True)

    class Meta:
        model = Mission
        fields = ["id", "cat", "is_complete", "targets"]

    @staticmethod
    def validate_targets(targets):
        if len(targets) < 1 or len(targets) > 3:
            raise serializers.ValidationError("A mission requires 1-3 targets")
        return targets

    def create(self, validated_data):
        targets_data = validated_data.pop("targets")
        mission = Mission.objects.create(**validated_data)

        mission.targets.set(targets_data)

        return mission
