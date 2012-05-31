from kant.node import K

K('official_group',
  'law enforcement', 'authorities', 'officials', 'disaster management')

K('american_agency',
  'DHS', 'Homeland Security',
  'DEA', 'Drug Enforcement Agency',
  'FDA', 'Federal Drug Administration',
  'FEMA', 'Federal Emergency Management',
  'CIA', 'Central Intelligence Agency',
  'DNDO', 'Domestic Nuclear Detection Office',
  'American {official_group}')

K('international_agency',
  'World Health Organization', 'NATO', 'U.N.', 'United Nations', 'World Bank')

K('agency',
  '{international_agency}', '{american_agency}')

K('middle_east_region',
  'Iraq', 'Afghanistan', 'Pakistan', 'Yemen', 'Somalia', 'Nigeria')

K('middle_east_regional_adj',
  'Iraqi', 'Afghani', 'Pakistani', 'Yemeni', 'Somalian', 'Nigerian')

K('south_american_region',
  'Mexico', 'Juarez', 'Sinaloa', 'Tijuana', 'Torreon', 'Yuma', 'Tucson', 'El Paso', 'Fort Hancock',
  'San Diego', 'Sonora', 'Columbia', 'Los Zetas')

K('south_american_regional_adj',
  'Mexcian', 'Columbian', 'American', 'South American')

K('bad_group_adj',
  'Drug', 'Weapon', 'Human-Trafficking', 'Terrorist')

K('bad_group_type',
  'Gang', 'Cartel', 'Cell', 'Organization')

K('bad_group',
  '{bad_group_adj} {bad_group_type}')

K('middle_east_bad_group',
  '{middle_east_regional_adj} {bad_group}')

K('south_american_bad_group',
  '{south_american_regional_adj} {bad_group}')

K('criminal_group',
  'Al Qaeda', 'Hamas', 'Armed Revolutionary Forces of Columbia', 'Irish Republican Army', 'Hezbollah',
  'Tamil Tigers', 'Palestine Liberation Front', 'Palestine Liberation Organization', 'Taliban',
  '{middle_east_bad_group}', '{south_american_bad_group}')


if "__main__" == __name__:
    headline = K('headline', '{criminal_group} Now Main Focus of {agency}')
    print headline
