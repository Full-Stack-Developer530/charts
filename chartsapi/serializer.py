from rest_framework import serializers
from .models import YearData


class CustomYearDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = YearData
        fields = ['year', 'month_data']

    def to_representation(self, instance):
        result = {
            instance.year: []
        }

        for month in instance.month_data.all():
            month_data = {month.month: []}

            for time_data in month.time_data.all():
                formatted_timestamp = time_data.timestamp.strftime("%Y/%m/%d , %H:%M:%S")
                month_data[month.month].append({formatted_timestamp: time_data.value})

            result[instance.year].append(month_data)

        return result
