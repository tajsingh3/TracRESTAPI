from rest_framework import serializers


class Sbu:
    def __init__(self, approved, unapproved, expired_yes, expired_no,
                 reg_yes, reg_no, freq_daily, freq_weekly, freq_monthly,
                 freq_annually):
        self.approved = approved
        self.unapproved = unapproved
        self.expired_yes = expired_yes
        self.expired_no = expired_no
        self.reg_yes = reg_yes
        self.reg_no = reg_no
        self.freq_daily = freq_daily
        self.freq_weekly = freq_weekly
        self.freq_monthly = freq_monthly
        self.freq_annually = freq_annually


class SbuSerializer(serializers.Serializer):
    approved = serializers.IntegerField()
    unapproved = serializers.IntegerField()
    expired_yes = serializers.IntegerField()
    expired_no = serializers.IntegerField()
    reg_yes = serializers.IntegerField()
    reg_no = serializers.IntegerField()
    freq_daily = serializers.IntegerField()
    freq_weekly = serializers.IntegerField()
    freq_monthly = serializers.IntegerField()
    freq_annually = serializers.IntegerField()


class SbuSet:
    def __init__(self, corporate, retail, treasury, financial, operations,
                 humanResources, investments, rmc, accounts, infotech):
        self.corporate = corporate
        self.retail = retail
        self.treasury = treasury
        self.financial = financial
        self.operations = operations
        self.humanResources = humanResources
        self.investments = investments
        self.rmc = rmc
        self.accounts = accounts
        self.infotech = infotech


class SbuSetSerializer(serializers.Serializer):
    corporate = SbuSerializer()
    retail = SbuSerializer()
    treasury = SbuSerializer()
    financial = SbuSerializer()
    operations = SbuSerializer()
    humanResources = SbuSerializer()
    investments = SbuSerializer()
    rmc = SbuSerializer()
    accounts = SbuSerializer()
    infotech = SbuSerializer()


class TracEntry:
    def __init__(self, serial, description, sbu, scope, reviewFrequency,
                 lastReviewDate, nextReviewDate, days, expired, regulatory,
                 approved, responsibility, note):
        self.serial = serial
        self.description = description
        self.sbu = sbu
        self.scope = scope
        self.reviewFrequency = reviewFrequency
        self.lastReviewDate = lastReviewDate
        self.nextReviewDate = nextReviewDate
        self.days = days
        self.expired = expired
        self.regulatory = regulatory
        self.approved = approved
        self.responsibility = responsibility
        self.note = note


class TracEntrySerializer(serializers.Serializer):
    serial = serializers.CharField(max_length=20)
    description = serializers.CharField(max_length=20)
    sbu = serializers.CharField(max_length=20)
    scope = serializers.CharField(max_length=20)
    reviewFrequency = serializers.CharField(max_length=20)
    lastReviewDate = serializers.CharField(max_length=20)
    nextReviewDate = serializers.CharField(max_length=20)
    days = serializers.CharField(max_length=20)
    expired = serializers.CharField(max_length=20)
    regulatory = serializers.CharField(max_length=20)
    approved = serializers.CharField(max_length=20)
    responsibility = serializers.CharField(max_length=20)
    note = serializers.CharField(max_length=20)
