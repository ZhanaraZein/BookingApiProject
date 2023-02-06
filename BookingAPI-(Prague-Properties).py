#!/usr/bin/env python
# coding: utf-8


# Libraries
import re
import time
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os
import argparse

def query(offset):
  # Request Query
  json_data = {
      'operationName': 'FullSearch',
      'variables': {
          'input': {
              'acidCarouselContext': None,
              'childrenAges': [],
              'doAvailabilityCheck': False,
              'encodedAutocompleteMeta': None,
              'enableCampaigns': True,
              'filters': {},
              'forcedBlocks': None,
              'location': {
                  'searchString': 'Prague',
                  'destType': 'CITY',
                  'destId': -553173,
              },
              'metaContext': None,
              'nbRooms': 1,
              'nbAdults': 1,
              'nbChildren': 0,
              'showAparthotelAsHotel': True,
              'needsRoomsMatch': False,
              'sbCalendarOpen': True,
              'optionalFeatures': {
                  'forceArpExperiments': True,
                  'testProperties': False,
              },
              'pagination': {
                  'rowsPerPage': 100,
                  'offset': offset,
              },
              'rawQueryForSession': '/searchresults.en-gb.html?label=gen173nr-1BCAEoggI46AdIM1gEaLUBiAEBmAEJuAEHyAEM2AEB6AEBiAIBqAIDuAK9xPmdBsACAdICJDlkYzZmNjg5LTE0ZjYtNDIzYy04NjVkLWRmOTYyNTE5M2MyMdgCBeACAQ&sid=dd84131c86d6702477f73e2ef27d68fd&aid=304142&ss=Prague&ssne=Prague&ssne_untouched=Prague&efdco=1&lang=en-gb&sb=1&src_elem=sb&src=searchresults&dest_id=-553173&dest_type=city&group_adults=1&no_rooms=1&group_children=0&sb_travel_purpose=leisure&offset=25',
              'referrerBlock': None,
              'sorters': {
                  'selectedSorter': None,
                  'referenceGeoId': None,
                  'tripTypeIntentId': None,
              },
              
              
              
              'travelPurpose': 2,
              'seoThemeIds': [],
              'useSearchParamsFromSession': True,
          },
          'geniusVipUI': {
              'enableEnroll': True,
          },
      },
      'extensions': {},
      'query': 'query FullSearch($input: SearchQueryInput!, $geniusVipUI: GeniusVipUIsInput) {\n  searchQueries {\n    search(input: $input) {\n      ...FullSearchFragment\n      __typename\n    }\n    __typename\n  }\n  geniusVipEnrolledProgram(input: $geniusVipUI) {\n    ...geniusVipEnrolledProgramFragment\n    __typename\n  }\n}\n\nfragment FullSearchFragment on SearchQueryOutput {\n  banners {\n    ...Banner\n    __typename\n  }\n  breadcrumbs {\n    ... on SearchResultsBreadcrumb {\n      ...SearchResultsBreadcrumb\n      __typename\n    }\n    ... on LandingPageBreadcrumb {\n      ...LandingPageBreadcrumb\n      __typename\n    }\n    __typename\n  }\n  carousels {\n    ...Carousel\n    __typename\n  }\n  destinationLocation {\n    ...DestinationLocation\n    __typename\n  }\n  entireHomesSearchEnabled\n  entireHomesSearchLabel\n  filters {\n    ...FilterData\n    __typename\n  }\n  recommendedFilterOptions {\n    ...FilterOption\n    __typename\n  }\n  pagination {\n    nbResultsPerPage\n    nbResultsTotal\n    __typename\n  }\n  tripTypes {\n    ...TripTypesData\n    __typename\n  }\n  results {\n    ...BasicPropertyData\n    ...MatchingUnitConfigurations\n    ...PropertyBlocks\n    ...BookerExperienceData\n    priceDisplayInfo {\n      ...PriceDisplayInfo\n      __typename\n    }\n    __typename\n  }\n  searchMeta {\n    ...SearchMetadata\n    __typename\n  }\n  sorters {\n    option {\n      ...SorterFields\n      __typename\n    }\n    __typename\n  }\n  oneOfThreeDeal {\n    ...OneOfThreeDeal\n    __typename\n  }\n  zeroResultsSection {\n    ...ZeroResultsSection\n    __typename\n  }\n  __typename\n}\n\nfragment BasicPropertyData on SearchResultProperty {\n  acceptsWalletCredit\n  basicPropertyData {\n    accommodationTypeId\n    id\n    isTestProperty\n    location {\n      address\n      city\n      countryCode\n      __typename\n    }\n    pageName\n    ufi\n    photos {\n      main {\n        highResUrl {\n          relativeUrl\n          __typename\n        }\n        lowResUrl {\n          relativeUrl\n          __typename\n        }\n        highResJpegUrl {\n          relativeUrl\n          __typename\n        }\n        lowResJpegUrl {\n          relativeUrl\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    reviewScore: reviews {\n      score: totalScore\n      reviewCount: reviewsCount\n      totalScoreTextTag {\n        translation\n        __typename\n      }\n      showScore\n      secondaryScore\n      secondaryTextTag {\n        translation\n        __typename\n      }\n      showSecondaryScore\n      __typename\n    }\n    externalReviewScore: externalReviews {\n      score: totalScore\n      reviewCount: reviewsCount\n      showScore\n      totalScoreTextTag {\n        translation\n        __typename\n      }\n      __typename\n    }\n    starRating {\n      value\n      symbol\n      caption {\n        translation\n        __typename\n      }\n      tocLink {\n        translation\n        __typename\n      }\n      showAdditionalInfoIcon\n      __typename\n    }\n    isClosed\n    paymentConfig {\n      installments {\n        minPriceFormatted\n        maxAcceptCount\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  badges {\n    caption {\n      translation\n      __typename\n    }\n    closedFacilities {\n      startDate\n      endDate\n      __typename\n    }\n    __typename\n  }\n  customBadges {\n    showIsWorkFriendly\n    showParkAndFly\n    showSkiToDoor\n    showBhTravelCreditBadge\n    showOnlineCheckinBadge\n    __typename\n  }\n  description {\n    text\n    __typename\n  }\n  displayName {\n    text\n    translationTag {\n      translation\n      __typename\n    }\n    __typename\n  }\n  geniusInfo {\n    benefitsCommunication {\n      header {\n        title\n        __typename\n      }\n      items {\n        title\n        __typename\n      }\n      __typename\n    }\n    geniusBenefits\n    geniusBenefitsData {\n      hotelCardHasFreeBreakfast\n      hotelCardHasFreeRoomUpgrade\n      sortedBenefits\n      __typename\n    }\n    showGeniusRateBadge\n    __typename\n  }\n  isInCompanyBudget\n  location {\n    displayLocation\n    mainDistance\n    publicTransportDistanceDescription\n    skiLiftDistance\n    beachDistance\n    nearbyBeachNames\n    beachWalkingTime\n    geoDistanceMeters\n    beachRatingScore\n    natureParkData {\n      closestNatureParkData {\n        distanceToClosestNaturePark\n        distanceType\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  mealPlanIncluded {\n    mealPlanType\n    text\n    __typename\n  }\n  persuasion {\n    autoextended\n    geniusRateAvailable\n    highlighted\n    preferred\n    preferredPlus\n    showNativeAdLabel\n    nativeAdId\n    nativeAdsCpc\n    nativeAdsTracking\n    bookedXTimesMessage\n    metaTrafficHighlightedPropertyLabel\n    __typename\n  }\n  policies {\n    showFreeCancellation\n    showNoPrepayment\n    enableJapaneseUsersSpecialCase\n    __typename\n  }\n  ribbon {\n    ribbonType\n    text\n    __typename\n  }\n  recommendedDate {\n    checkin\n    checkout\n    lengthOfStay\n    __typename\n  }\n  showGeniusLoginMessage\n  showPrivateHostMessage\n  soldOutInfo {\n    isSoldOut\n    messages {\n      translationTag {\n        translation\n        __typename\n      }\n      __typename\n    }\n    alternativeDatesMessages {\n      translationTag {\n        translation\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  nbWishlists\n  visibilityBoosterEnabled\n  showAdLabel\n  isNewlyOpened\n  propertySustainability {\n    isSustainable\n    tier {\n      type\n      __typename\n    }\n    facilities {\n      id\n      __typename\n    }\n    certifications {\n      name\n      __typename\n    }\n    chainProgrammes {\n      chainName\n      programmeName\n      __typename\n    }\n    levelId\n    __typename\n  }\n  seoThemes {\n    caption\n    __typename\n  }\n  relocationMode {\n    distanceToCityCenterKm\n    distanceToCityCenterMiles\n    distanceToOriginalHotelKm\n    distanceToOriginalHotelMiles\n    phoneNumber\n    __typename\n  }\n  bundleRatesAvailable\n  __typename\n}\n\nfragment Banner on Banner {\n  name\n  type\n  isDismissible\n  showAfterDismissedDuration\n  position\n  requestAlternativeDates\n  title {\n    text\n    __typename\n  }\n  imageUrl\n  paragraphs {\n    text\n    __typename\n  }\n  metadata {\n    key\n    value\n    __typename\n  }\n  pendingReviewInfo {\n    propertyPhoto {\n      lowResUrl {\n        relativeUrl\n        __typename\n      }\n      lowResJpegUrl {\n        relativeUrl\n        __typename\n      }\n      __typename\n    }\n    propertyName\n    urlAccessCode\n    __typename\n  }\n  nbDeals\n  primaryAction {\n    text {\n      text\n      __typename\n    }\n    action {\n      name\n      context {\n        key\n        value\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  flexibleFilterOptions {\n    optionId\n    filterName\n    __typename\n  }\n  trackOnView {\n    type\n    experimentHash\n    value\n    __typename\n  }\n  __typename\n}\n\nfragment Carousel on Carousel {\n  aggregatedCountsByFilterId\n  carouselId\n  position\n  contentType\n  hotelId\n  name\n  soldoutProperties\n  priority\n  themeId\n  title {\n    text\n    __typename\n  }\n  slides {\n    captionText {\n      text\n      __typename\n    }\n    name\n    photoUrl\n    subtitle {\n      text\n      __typename\n    }\n    type\n    title {\n      text\n      __typename\n    }\n    action {\n      context {\n        key\n        value\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment DestinationLocation on DestinationLocation {\n  name {\n    text\n    __typename\n  }\n  inName {\n    text\n    __typename\n  }\n  countryCode\n  __typename\n}\n\nfragment FilterData on Filter {\n  trackOnView {\n    type\n    experimentHash\n    value\n    __typename\n  }\n  trackOnClick {\n    type\n    experimentHash\n    value\n    __typename\n  }\n  name\n  field\n  category\n  filterStyle\n  title {\n    text\n    translationTag {\n      translation\n      __typename\n    }\n    __typename\n  }\n  options {\n    trackOnView {\n      type\n      experimentHash\n      value\n      __typename\n    }\n    trackOnClick {\n      type\n      experimentHash\n      value\n      __typename\n    }\n    trackOnSelect {\n      type\n      experimentHash\n      value\n      __typename\n    }\n    trackOnDeSelect {\n      type\n      experimentHash\n      value\n      __typename\n    }\n    trackOnViewPopular {\n      type\n      experimentHash\n      value\n      __typename\n    }\n    trackOnClickPopular {\n      type\n      experimentHash\n      value\n      __typename\n    }\n    trackOnSelectPopular {\n      type\n      experimentHash\n      value\n      __typename\n    }\n    trackOnDeSelectPopular {\n      type\n      experimentHash\n      value\n      __typename\n    }\n    ...FilterOption\n    __typename\n  }\n  filterLayout {\n    isCollapsable\n    collapsedCount\n    __typename\n  }\n  stepperOptions {\n    min\n    max\n    default\n    selected\n    title {\n      text\n      translationTag {\n        translation\n        __typename\n      }\n      __typename\n    }\n    field\n    labels {\n      translationTag {\n        translation\n        __typename\n      }\n      __typename\n    }\n    trackOnView {\n      type\n      experimentHash\n      value\n      __typename\n    }\n    trackOnClick {\n      type\n      experimentHash\n      value\n      __typename\n    }\n    trackOnSelect {\n      type\n      experimentHash\n      value\n      __typename\n    }\n    trackOnDeSelect {\n      type\n      experimentHash\n      value\n      __typename\n    }\n    trackOnClickDecrease {\n      type\n      experimentHash\n      value\n      __typename\n    }\n    trackOnClickIncrease {\n      type\n      experimentHash\n      value\n      __typename\n    }\n    trackOnDecrease {\n      type\n      experimentHash\n      value\n      __typename\n    }\n    trackOnIncrease {\n      type\n      experimentHash\n      value\n      __typename\n    }\n    __typename\n  }\n  sliderOptions {\n    min\n    max\n    minSelected\n    maxSelected\n    minPriceStep\n    minSelectedFormatted\n    currency\n    histogram\n    selectedRange {\n      translation\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment FilterOption on Option {\n  optionId: id\n  count\n  selected\n  urlId\n  additionalLabel {\n    text\n    translationTag {\n      translation\n      __typename\n    }\n    __typename\n  }\n  value {\n    text\n    translationTag {\n      translation\n      __typename\n    }\n    __typename\n  }\n  starRating {\n    value\n    symbol\n    caption {\n      translation\n      __typename\n    }\n    showAdditionalInfoIcon\n    __typename\n  }\n  __typename\n}\n\nfragment LandingPageBreadcrumb on LandingPageBreadcrumb {\n  destType\n  name\n  urlParts\n  __typename\n}\n\nfragment MatchingUnitConfigurations on SearchResultProperty {\n  matchingUnitConfigurations {\n    commonConfiguration {\n      name\n      unitId\n      bedConfigurations {\n        beds {\n          count\n          type\n          __typename\n        }\n        nbAllBeds\n        __typename\n      }\n      nbAllBeds\n      nbBathrooms\n      nbBedrooms\n      nbKitchens\n      nbLivingrooms\n      nbUnits\n      unitTypeNames {\n        translation\n        __typename\n      }\n      localizedArea {\n        localizedArea\n        unit\n        __typename\n      }\n      __typename\n    }\n    unitConfigurations {\n      name\n      unitId\n      bedConfigurations {\n        beds {\n          count\n          type\n          __typename\n        }\n        nbAllBeds\n        __typename\n      }\n      apartmentRooms {\n        config {\n          roomId: id\n          roomType\n          bedTypeId\n          bedCount: count\n          __typename\n        }\n        roomName: tag {\n          tag\n          translation\n          __typename\n        }\n        __typename\n      }\n      nbAllBeds\n      nbBathrooms\n      nbBedrooms\n      nbKitchens\n      nbLivingrooms\n      nbUnits\n      unitTypeNames {\n        translation\n        __typename\n      }\n      localizedArea {\n        localizedArea\n        unit\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment PropertyBlocks on SearchResultProperty {\n  blocks {\n    blockId {\n      roomId\n      occupancy\n      policyGroupId\n      packageId\n      mealPlanId\n      __typename\n    }\n    finalPrice {\n      amount\n      currency\n      __typename\n    }\n    originalPrice {\n      amount\n      currency\n      __typename\n    }\n    onlyXLeftMessage {\n      tag\n      variables {\n        key\n        value\n        __typename\n      }\n      translation\n      __typename\n    }\n    freeCancellationUntil\n    hasCrib\n    blockMatchTags {\n      childStaysForFree\n      __typename\n    }\n    thirdPartyInventoryContext {\n      isTpiBlock\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment PriceDisplayInfo on PriceDisplayInfo {\n  badges {\n    name {\n      translation\n      __typename\n    }\n    tooltip {\n      translation\n      __typename\n    }\n    style\n    identifier\n    __typename\n  }\n  chargesInfo {\n    translation\n    __typename\n  }\n  displayPrice {\n    copy {\n      translation\n      __typename\n    }\n    amountPerStay {\n      amount\n      amountRounded\n      amountUnformatted\n      currency\n      __typename\n    }\n    __typename\n  }\n  priceBeforeDiscount {\n    copy {\n      translation\n      __typename\n    }\n    amountPerStay {\n      amount\n      amountRounded\n      amountUnformatted\n      currency\n      __typename\n    }\n    __typename\n  }\n  rewards {\n    rewardsList {\n      termsAndConditions\n      amountPerStay {\n        amount\n        amountRounded\n        amountUnformatted\n        currency\n        __typename\n      }\n      breakdown {\n        productType\n        amountPerStay {\n          amount\n          amountRounded\n          amountUnformatted\n          currency\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    rewardsAggregated {\n      amountPerStay {\n        amount\n        amountRounded\n        amountUnformatted\n        currency\n        __typename\n      }\n      copy {\n        translation\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  useRoundedAmount\n  discounts {\n    amount {\n      amount\n      amountRounded\n      amountUnformatted\n      currency\n      __typename\n    }\n    name {\n      translation\n      __typename\n    }\n    description {\n      translation\n      __typename\n    }\n    itemType\n    __typename\n  }\n  excludedCharges {\n    excludeChargesAggregated {\n      copy {\n        translation\n        __typename\n      }\n      amountPerStay {\n        amount\n        amountRounded\n        amountUnformatted\n        currency\n        __typename\n      }\n      __typename\n    }\n    excludeChargesList {\n      chargeMode\n      chargeInclusion\n      amountPerStay {\n        amount\n        amountRounded\n        amountUnformatted\n        currency\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  taxExceptions {\n    shortDescription {\n      translation\n      __typename\n    }\n    longDescription {\n      translation\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment BookerExperienceData on SearchResultProperty {\n  bookerExperienceContentUIComponentProps {\n    ... on BookerExperienceContentLoyaltyBadgeListProps {\n      badges {\n        variant\n        key\n        title\n        popover\n        logoSrc\n        logoAlt\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment SearchMetadata on SearchMeta {\n  availabilityInfo {\n    hasLowAvailability\n    unavailabilityPercent\n    totalAvailableNotAutoextended\n    __typename\n  }\n  boundingBoxes {\n    swLat\n    swLon\n    neLat\n    neLon\n    type\n    __typename\n  }\n  childrenAges\n  dates {\n    checkin\n    checkout\n    lengthOfStayInDays\n    maxLengthOfStayInDays\n    __typename\n  }\n  destId\n  destType\n  nbRooms\n  nbAdults\n  nbChildren\n  userHasSelectedFilters\n  customerValueStatus\n  affiliatePartnerChannelId\n  affiliatePartnerId\n  __typename\n}\n\nfragment SearchResultsBreadcrumb on SearchResultsBreadcrumb {\n  destId\n  destType\n  name\n  __typename\n}\n\nfragment SorterFields on SorterOption {\n  type: name\n  captionTranslationTag {\n    translation\n    __typename\n  }\n  tooltipTranslationTag {\n    translation\n    __typename\n  }\n  isSelected: selected\n  __typename\n}\n\nfragment OneOfThreeDeal on OneOfThreeDeal {\n  id\n  uuid\n  winnerHotelId\n  winnerBlockId\n  priceDisplayInfo {\n    displayPrice {\n      amountPerStay {\n        amountRounded\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  locationInfo {\n    name\n    inName\n    destType\n    __typename\n  }\n  destinationType\n  commonFacilities {\n    id\n    name\n    __typename\n  }\n  properties {\n    priceDisplayInfo {\n      priceBeforeDiscount {\n        amountPerStay {\n          amountRounded\n          __typename\n        }\n        __typename\n      }\n      displayPrice {\n        amountPerStay {\n          amountRounded\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    basicPropertyData {\n      id\n      name\n      pageName\n      photos {\n        main {\n          highResUrl {\n            absoluteUrl\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      location {\n        address\n        countryCode\n        __typename\n      }\n      reviews {\n        reviewsCount\n        totalScore\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment TripTypesData on TripTypes {\n  beach {\n    isBeachUfi\n    isEnabledBeachUfi\n    isCoastalBeachRegion\n    isBeachDestinationWithoutBeach\n    __typename\n  }\n  ski {\n    isSkiExperience\n    isSkiScaleUfi\n    __typename\n  }\n  skiResorts {\n    name\n    resortId\n    localizedTrailDistance\n    photoUrl\n    __typename\n  }\n  carouselBeach {\n    name\n    beachId\n    photoUrl\n    reviewScore\n    reviewScoreFormatted\n    translatedBeachActivities\n    translatedSandType\n    __typename\n  }\n  highestTrafficSkiRegionOfMultiRegionLowAVUfi {\n    regionId\n    regionName\n    photoUrl\n    skiRegionUfiData {\n      cityName\n      __typename\n    }\n    __typename\n  }\n  skiLandmarkData {\n    resortId\n    slopeTotalLengthFormatted\n    totalLiftsCount\n    __typename\n  }\n  __typename\n}\n\nfragment ZeroResultsSection on ZeroResultsSection {\n  title {\n    text\n    __typename\n  }\n  primaryAction {\n    text {\n      text\n      __typename\n    }\n    action {\n      name\n      __typename\n    }\n    __typename\n  }\n  paragraphs {\n    text\n    __typename\n  }\n  type\n  __typename\n}\n\nfragment geniusVipEnrolledProgramFragment on GeniusVipEnrolledProgram {\n  metadata {\n    programType\n    __typename\n  }\n  geniusVipUIs {\n    searchResultModal {\n      title {\n        text\n        __typename\n      }\n      subtitle {\n        text\n        __typename\n      }\n      modalCategory\n      asset {\n        __typename\n        ... on Image {\n          url\n          __typename\n        }\n      }\n      cta {\n        text\n        actionString\n        actionDismiss\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n',
  }
  return json_data

def getResults():
    # Headers
    headers = {
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Origin': 'https://www.booking.com',
        'Referer': 'https://www.booking.com/searchresults.en-gb.html?label=gen173nr-1BCAEoggI46AdIM1gEaLUBiAEBmAEJuAEHyAEM2AEB6AEBiAIBqAIDuAK9xPmdBsACAdICJDlkYzZmNjg5LTE0ZjYtNDIzYy04NjVkLWRmOTYyNTE5M2MyMdgCBeACAQ&sid=dd84131c86d6702477f73e2ef27d68fd&aid=304142&ss=Prague&ssne=Prague&ssne_untouched=Prague&efdco=1&lang=en-gb&sb=1&src_elem=sb&src=searchresults&dest_id=-553173&dest_type=city&group_adults=1&no_rooms=1&group_children=0&sb_travel_purpose=leisure&offset=25',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'accept': '*/*',
        'content-type': 'application/json',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'x-booking-context-action-name': 'searchresults_irene',
        'x-booking-context-aid': '304142',
        'x-booking-csrf-token': 'eyJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJjb250ZXh0LWVucmljaG1lbnQtYXBpIiwic3ViIjoiY3NyZi10b2tlbiIsImlhdCI6MTY3MzQyMTUwMywiZXhwIjoxNjczNTA3OTAzfQ.O-E37yonSqKx3RuoFDkGAWrCHbYS-lY2UXdrYesnTkTTGzZodSaH5DelZ6czQ9BC-aNYmFb1aJK0b-rMEgykFg',
        'x-booking-et-serialized-state': 'Egpj8VUSf_gj5c3Er0faHJXODjBQQF4-6qXaEiO_2JpwusJpAivxWdEwi4IqmN0u6',
        'x-booking-pageview-id': 'af48335f88300013',
        'x-booking-site-type-id': '1',
        'x-booking-topic': 'capla_browser_b-search-web-searchresults',
    }

    # Parameters
    params = {
        'ss': 'Prague',
        'ssne': 'Prague',
        'ssne_untouched': 'Prague',
        'efdco': '1',
        'label': 'gen173nr-1BCAEoggI46AdIM1gEaLUBiAEBmAEJuAEHyAEM2AEB6AEBiAIBqAIDuAK9xPmdBsACAdICJDlkYzZmNjg5LTE0ZjYtNDIzYy04NjVkLWRmOTYyNTE5M2MyMdgCBeACAQ',
        'sid': 'dd84131c86d6702477f73e2ef27d68fd',
        'aid': '304142',
        'lang': 'en-gb',
        'sb': '1',
        'src_elem': 'sb',
        'src': 'searchresults',
        'dest_id': '-553173',
        'dest_type': 'city',
        'group_adults': '1',
        'no_rooms': '1',
        'group_children': '0',
        'sb_travel_purpose': 'leisure',
    }

    results = []

    for offset in range(0, 2001, 100):
      json_data = query(offset)
      response = requests.post('https://www.booking.com/dml/graphql', params=params, headers=headers, json=json_data).json()
      results.append(response['data']['searchQueries']['search']['results'])
      time.sleep(0.1)
      print("Done: {}".format(offset))

    results = [res for result in results for res in result]

    return results;

def handleStarRaitingData(data):
    if data:
        return data['value']
    
    return 0

def handleEstablishmentData(data):
    if "hotel" in data.lower():
        data = "Hotel"
        
    elif "apartment" in data.lower():
        data = "Apartment"
        
    elif "maison" in data.lower():
        data = "Maison"
        
    elif "boutique" in data.lower():
        data = "Boutique"
        
    elif "residence" in data.lower():
        data = "Residence"
        
    else:
        data = "other"

    return data

def handleDistrictData(data):
    replacedValues = [
        "Praha",
        "Praze",
        "praha",
        "Prag",
        "Pra-ha",
        "Прага",
        "Pragueue"
    ]

    data = data.strip()

    for replacedValue in replacedValues:
        data = data.replace(replacedValue, "Prague")

    search = re.search(r"(Prague \d+)", data)

    if search:
        data = search.group()

    return data

def handleDistanceData(data):
    data = re.findall(r"[-+]?(?:\d*\.*\d+)", data)[0]

    if float(data).is_integer():
        data = float(data) / 1000
    
    return float(data)

def get(data):
    return {
      "Establishment": handleEstablishmentData(data['description']['text']),
      "Rating": data['basicPropertyData']['reviewScore']['secondaryScore'],
      "Review Count": data['basicPropertyData']['reviewScore']['reviewCount'],
      "Address": data['basicPropertyData']['location']['address'],
      "countryCode": data['basicPropertyData']['location']['countryCode'],
      "District": handleDistrictData(data['location']['displayLocation']),
      "Star Rating": handleStarRaitingData(data['basicPropertyData']['starRating']),
      "Distance": handleDistanceData(data['location']['mainDistance']),
      "Level": data['propertySustainability']['levelId'],
      "type": data['propertySustainability']['tier']['type'],
      "image": "https://cf.bstatic.com"+data['basicPropertyData']['photos']['main']['highResJpegUrl']['relativeUrl']
    }

def getCleanedData():

    cleaned = []

    results = getResults()

    for result in results:
        cleaned.append(get(result))

    return cleaned

def getRefinedData():

    data = pd.DataFrame.from_records(getCleanedData())

    refined = data[~data.duplicated()]
    
    refined.to_csv("./data/booking_api_prague.csv")
    
    refined = refined[refined['District'].str.extract('(\d+)').notnull().any(axis='columns')]
    
    refined.drop(["type", "countryCode", "image"], inplace=True, axis=1)
    
    refined.head()

    refined.columns = ["Establishment", "Rating", "Review Count", "Address", "District", "Star Rating", "Distance", "Level"]
    
    return refined

def createStarRatingPlot(path, data):
    sort1=data.sort_values("District")
    plt.figure(figsize=(30, 9))
    plt.bar(sort1['District'], data['Star Rating'])
    plt.xlabel('District', fontsize = 20)
    plt.ylabel('Star Rating', fontsize = 20)
    plt.title("Star Ratings w.r.t District", fontsize = 30)
    plt.xticks(rotation=45, ha='right', fontsize = 15)
    plt.yticks(fontsize = 15)
    plt.savefig(path + "/Star_Ratings_w.r.t_District.jpg")

def createEstablishmentTypePieChart(path, data):
    # create a pie chart of the Establishment Types
    plt.figure(figsize=(10, 10))
    level_counts = data['Establishment'].value_counts()
    plt.pie(level_counts.values, labels=level_counts.index, autopct='%1.2f%%')
    plt.title("Distribution of Establishment Types")
    plt.savefig(path + "/Distribution_of_Establishment_Types.jpg")

def createReviewCountHistogram(path, data):
    # create a histogram of the review count
    plt.figure(figsize=(12, 9))
    plt.hist(data['Review Count'], bins=20, color="green")
    plt.xlabel('Review Count')
    plt.ylabel('Frequency')
    plt.title("Distribution of Reviews in Properties")
    plt.savefig(path + "/Distribution_of_Reviews_in_Properties.jpg")

def createStarRatingBoxPlot(path, data):
    # create a box plot of the star rating
    plt.figure(figsize=(12, 9))
    data.boxplot(column='Star Rating', by='District', figsize=(12, 9))
    plt.xticks(rotation=45, ha='right')
    plt.savefig(path + "/Box_plot_Star_Rating_vs._District.jpg")

def createEstablishmentBarChart(path, data):
    # create a stacked bar chart of the Establishment by city
    level_counts = data.groupby(['District', 'Establishment']).size().reset_index(name='counts')
    level_counts = level_counts.pivot(index='District', columns='Establishment', values='counts')
    level_counts.plot(kind='bar', stacked=True, figsize=(25, 12))
    plt.title("Bar Chart w.r.t District vs Establishment", fontsize = 30)
    plt.xlabel('District', fontsize = 20)
    plt.ylabel('Count',  fontsize = 20)
    plt.xticks(rotation=45, ha='right', fontsize = 15)
    plt.yticks(fontsize = 15)
    plt.savefig(path + "/Bar_Chart_w.r.t_District_vs_Establishment.jpg")

def createReviewCountHeatMap(path, data):
    #create a heat map of  review count and distance
    plt.figure(figsize=(12, 9))
    plt.hist2d(data['Review Count'], data['Distance'].astype("float32"))
    plt.xlabel('Review Count')
    plt.ylabel('Distance')
    plt.title("Intensity of Reviews w.r.t Distance")
    plt.colorbar()
    plt.savefig(path + "/Intensity_of_Reviews_w.r.t_Distance.jpg")

def createRatingsPlot(path, data):
    plt.figure(figsize=(30, 9))
    plt.bar(data['District'], data['Rating'])
    plt.xlabel('District', fontsize = 20)
    plt.ylabel('Rating', fontsize = 20)
    plt.title("Ratings w.r.t District", fontsize = 30)
    plt.xticks(rotation=45, ha='right', fontsize = 15)
    plt.yticks(fontsize = 15)
    plt.savefig(path + "/Ratings_w.r.t_District.jpg")

def createReviewCountVsDistanceScatterPlot(path, data):
    # create a scatter plot of review count and distance with hovers
    sort = data.sort_values("Distance")
    fig = px.scatter(sort, x='Review Count', y='Distance', hover_data=['Establishment', 'Rating', 'District', 'Star Rating'])
    fig.write_image(path + "/Scatter_plot_Review_Count_vs._Distance.png")

def createReviewCountVsStarRatingScatterPlot(path, data):
    figB = px.scatter(data, x='Review Count', y='Star Rating', hover_data=['Establishment', 'Rating', 'District', 'Star Rating'])
    figB.write_image(path + "/Scatter_plot_Review_Count_vs._Star_Rating.png")

def createPlots(path, data):
    createStarRatingPlot(path, data)
    createEstablishmentTypePieChart(path, data)
    createReviewCountHistogram(path, data)
    createStarRatingBoxPlot(path, data)
    createEstablishmentBarChart(path, data)
    createReviewCountHeatMap(path, data)
    createRatingsPlot(path, data)
    createReviewCountVsDistanceScatterPlot(path, data)
    createReviewCountVsStarRatingScatterPlot(path, data)
    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('outdir', type=str, help='Output dir for plots')
    args = parser.parse_args()

    plotsDir = "./data/" + args.outdir

    isExist = os.path.exists(plotsDir)
    if not isExist:
        #Create a new directory because it does not exist
        os.makedirs(plotsDir)
        print("The new directory " + plotsDir + " is created!")

    createPlots(plotsDir, getRefinedData())
    
main()