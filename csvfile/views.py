from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .sbu import Sbu
from .serializers import SbuSet
from .serializers import SbuSetSerializer
from .serializers import TracEntrySerializer
from .tracentry import TracEntry, create_trac_entry_dataframe, create_trac_entry_objects
from .sbu import CSV_PATH, create_dataframe
import pandas as pd
from .tracentry import SBU_MAPPER



@csrf_exempt
def sbu_set(request):
    if request.method == 'GET':
        dataframe = create_dataframe(CSV_PATH)
        sbus = pd.unique(dataframe['sbu'])

        sbu_policy_objects_list = []
        for sbu in sbus:
            sbu_policy_objects_list.append(Sbu(sbu, 'Policy'))

        for sbu_object in sbu_policy_objects_list:
            sbu_object.populate_counts(dataframe)

        for sbu_object in sbu_policy_objects_list:
            if sbu_object.name == 'Retail':
                retail = sbu_object
            elif sbu_object.name == 'Corporate':
                corporate = sbu_object
            elif sbu_object.name == 'Treasury':
                treasury = sbu_object
            elif sbu_object.name == 'Financial':
                financial = sbu_object
            elif sbu_object.name == 'Operations':
                operations = sbu_object
            elif sbu_object.name == 'Human resources':
                humanResources = sbu_object
            elif sbu_object.name == 'Investments':
                investments = sbu_object
            elif sbu_object.name == 'RMC':
                rmc = sbu_object
            elif sbu_object.name == 'Accounts':
                accounts = sbu_object
            else:
                infotech=sbu_object

        set = SbuSet(corporate, retail, treasury,financial,operations,
                     humanResources,investments,rmc,accounts,infotech)

        serialized_set = SbuSetSerializer(set)
        return JsonResponse(serialized_set.data, safe=False)


@csrf_exempt
def trac_entries(request, description, sbu, counter):
    if request.method == 'GET':
        dataframe = create_dataframe(CSV_PATH)
        dataframe = create_trac_entry_dataframe(dataframe, description, sbu, counter)
        trac_entries = create_trac_entry_objects(dataframe)

        serialized_entries = TracEntrySerializer(trac_entries, many=True)
        return JsonResponse(serialized_entries.data, safe=False)
