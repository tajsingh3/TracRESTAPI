from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import Sbu
from .serializers import SbuSet
from .serializers import SbuSetSerializer
from .serializers import TracEntrySerializer
from .tracentry import TracEntry, create_trac_entry_dataframe, create_trac_entry_objects
from .sbu import CSV_PATH, create_dataframe


@csrf_exempt
def sbu_set(request):
    if request.method == 'GET':
        corporate = Sbu(1, 1, 1, 0, 0, 1, 0, 0, 0, 0)
        retail = Sbu(2, 0, 0, 0, 0, 2, 0, 0, 0, 0)

        set = SbuSet(corporate, retail)
        serialized_set = SbuSetSerializer(set)
        return JsonResponse(serialized_set.data, safe=False)


@csrf_exempt
def trac_entries(request, description, sbu, counter):
    if request.method == 'GET':
        dataframe = create_dataframe(CSV_PATH)
        print(CSV_PATH)
        dataframe = create_trac_entry_dataframe(dataframe,description,sbu,counter)
        trac_entries = create_trac_entry_objects(dataframe)

        serialized_entries=TracEntrySerializer(trac_entries,many=True)
        return JsonResponse(serialized_entries.data, safe=False)