import pandas as pd
from sqlalchemy import create_engine
from MyCreds.mycreds import Capstone_AWS_SG


class DatabaseHelpers:
    engine = create_engine(f'postgresql+psycopg2://{Capstone_AWS_SG.username}:{Capstone_AWS_SG.password}@{Capstone_AWS_SG.host}/Capstone', echo=False)
    features = ['building_id',  # for url change.  Must drop before use in model predictions
                'storey_range_min',
                'storey_range_max',
                'n_rooms',
                'floor_area_sqm',
                'remaining_lease_years',
                'num_preschools_400m',
                'num_preschools_1km',
                'num_primary_schools_1km',
                'score_primary_schools_1km',
                'num_primary_schools_2km',
                'score_primary_schools_2km',
                'num_secondary_schools_1km',
                'score_secondary_schools_1km',
                'num_secondary_schools_2km',
                'score_secondary_schools_2km',
                'num_healthcare_2km',
                'num_healthcare_5km',
                'nearest_healthcare_clinc',
                'nearest_police',
                'nearest_fire',
                'num_maj_parks_1km',
                'num_maj_parks_2km',
                'nearest_maj_park',
                'num_min_parks_1km',
                'num_min_parks_2km',
                'nearest_min_park',
                'num_waterbodies_100m',
                'num_waterbodies_500m',
                'nearest_waterbody',
                'num_supermarket_1_5km',
                'nearest_supermarket',
                'num_wetmarket_1_5km',
                'nearest_wetmarket',
                'nearest_expressway',
                'nearest_expressway_entrance_exit',
                'num_busstops_100m',
                'num_busstops_400m',
                'nearest_busstop',
                'num_taxistands_100m',
                'num_taxistands_400m',
                'nearest_taxistand',
                'num_transit_stations_1_5km',
                'score_stations_1_5km',
                'nearest_transit_station',
                'num_transit_exits_100m',
                'num_transit_exits_400m',
                'dist_to_nearest_transit_exit',
                'num_malls_1_5km',
                'nearest_mall',
                'num_hawker_1_5km',
                'nearest_hawker',
                'dist_to_central_business_district',
                'dist_to_holland_village',
                'dist_to_dempsey_hill',
                'dist_to_serangoon_gardens_circus',
                'dist_to_orchard',
                'dist_to_arab_street',
                'dist_to_thomson_ridge',
                'dist_to_east_coast_park',
                'dist_to_bishan_park',
                'dist_to_botanic_gardens',
                'dist_to_hort_park',
                'dist_to_sentosa',
                'dist_to_gardens_by_the_bay',
                'dist_to_con_area_id_1',
                'dist_to_con_area_id_2',
                'dist_to_con_area_id_3',
                'dist_to_con_area_id_4',
                'dist_to_con_area_id_5',
                'dist_to_con_area_id_6',
                'dist_to_con_area_id_7',
                'dist_to_con_area_id_8',
                'dist_to_con_area_id_9',
                'dist_to_con_area_id_10',
                'dist_to_con_area_id_11',
                'dist_to_con_area_id_12',
                'dist_to_con_area_id_13',
                'dist_to_con_area_id_14',
                'dist_to_con_area_id_15',
                'dist_to_con_area_id_16',
                'dist_to_con_area_id_17',
                'dist_to_con_area_id_18',
                'dist_to_con_area_id_19',
                'dist_to_con_area_id_20',
                'dist_to_con_area_id_21',
                'dist_to_con_area_id_22',
                'dist_to_con_area_id_23',
                'dist_to_con_area_id_24',
                'dist_to_con_area_id_25',
                'dist_to_con_area_id_26',
                'dist_to_con_area_id_27',
                'dist_to_con_area_id_28',
                'dist_to_con_area_id_29',
                'dist_to_con_area_id_30',
                'dist_to_con_area_id_31',
                'dist_to_con_area_id_32',
                'dist_to_con_area_id_33',
                'dist_to_con_area_id_34',
                'dist_to_con_area_id_35',
                'dist_to_con_area_id_36',
                'dist_to_con_area_id_37',
                'dist_to_con_area_id_38',
                'dist_to_con_area_id_39',
                'dist_to_con_area_id_40',
                'dist_to_con_area_id_41',
                'dist_to_con_area_id_42',
                'dist_to_con_area_id_43',
                'dist_to_con_area_id_44',
                'dist_to_con_area_id_45',
                'dist_to_con_area_id_46',
                'dist_to_con_area_id_47',
                'dist_to_con_area_id_48',
                'dist_to_con_area_id_49',
                'dist_to_con_area_id_50',
                'dist_to_con_area_id_51',
                'dist_to_con_area_id_52',
                'dist_to_con_area_id_53',
                'dist_to_con_area_id_54',
                'dist_to_con_area_id_55',
                'dist_to_con_area_id_56',
                'dist_to_con_area_id_57',
                'dist_to_con_area_id_58',
                'dist_to_con_area_id_59',
                'dist_to_con_area_id_60',
                'dist_to_con_area_id_61',
                'dist_to_con_area_id_62',
                'dist_to_con_area_id_63',
                'dist_to_con_area_id_64',
                'dist_to_con_area_id_65',
                'dist_to_con_area_id_66',
                'dist_to_con_area_id_67',
                'dist_to_con_area_id_68',
                'dist_to_con_area_id_69',
                'dist_to_con_area_id_70',
                'dist_to_con_area_id_71',
                'dist_to_con_area_id_72',
                'dist_to_con_area_id_73',
                'dist_to_con_area_id_74',
                'dist_to_con_area_id_75',
                'dist_to_con_area_id_76',
                'dist_to_con_area_id_77',
                'dist_to_con_area_id_78',
                'dist_to_con_area_id_79',
                'dist_to_con_area_id_80',
                'dist_to_con_area_id_81',
                'dist_to_con_area_id_82',
                'dist_to_con_area_id_83',
                'dist_to_con_area_id_84',
                'dist_to_con_area_id_85',
                'dist_to_con_area_id_86',
                'dist_to_con_area_id_87',
                'dist_to_con_area_id_88',
                'dist_to_con_area_id_89',
                'dist_to_con_area_id_90',
                'dist_to_con_area_id_91',
                'dist_to_con_area_id_92',
                'dist_to_con_area_id_93',
                'dist_to_con_area_id_94',
                'dist_to_con_area_id_95',
                'dist_to_con_area_id_96',
                'dist_to_con_area_id_97',
                'dist_to_con_area_id_98',
                'dist_to_con_area_id_99',
                'dist_to_con_area_id_100',
                'dist_to_con_area_id_101',
                'dist_to_con_area_id_102',
                'dist_to_con_area_id_103',
                'dist_to_con_area_id_104',
                'dist_to_con_area_id_105',
                'dist_to_con_area_id_106',
                'dist_to_con_area_id_107',
                'dist_to_con_area_id_108',
                'dist_to_con_area_id_109',
                'dist_to_con_area_id_110',
                'dist_to_con_area_id_111',
                'dist_to_con_area_id_112',
                'dist_to_con_area_id_113',
                'dist_to_con_area_id_114',
                'dist_to_con_area_id_115',
                'dist_to_con_area_id_116',
                'dist_to_con_area_id_117',
                'dist_to_con_area_id_118',
                'dist_to_con_area_id_119',
                'dist_to_con_area_id_120',
                'dist_to_con_area_id_249',
                'dist_to_con_area_id_250',
                'dist_to_con_area_id_251',
                'dist_to_con_area_id_252',
                'dist_to_con_area_id_253',
                'dist_to_con_area_id_254',
                'dist_to_con_area_id_121',
                'dist_to_con_area_id_122',
                'dist_to_con_area_id_123',
                'dist_to_con_area_id_124',
                'dist_to_con_area_id_125',
                'dist_to_con_area_id_126',
                'dist_to_con_area_id_127',
                'dist_to_con_area_id_128',
                'dist_to_con_area_id_129',
                'dist_to_con_area_id_130',
                'dist_to_con_area_id_131',
                'dist_to_con_area_id_132',
                'dist_to_con_area_id_133',
                'dist_to_con_area_id_134',
                'dist_to_con_area_id_135',
                'dist_to_con_area_id_136',
                'dist_to_con_area_id_137',
                'dist_to_con_area_id_138',
                'dist_to_con_area_id_139',
                'dist_to_con_area_id_140',
                'dist_to_con_area_id_141',
                'dist_to_con_area_id_142',
                'dist_to_con_area_id_143',
                'dist_to_con_area_id_144',
                'dist_to_con_area_id_145',
                'dist_to_con_area_id_146',
                'dist_to_con_area_id_147',
                'dist_to_con_area_id_148',
                'dist_to_con_area_id_149',
                'dist_to_con_area_id_150',
                'dist_to_con_area_id_151',
                'dist_to_con_area_id_152',
                'dist_to_con_area_id_153',
                'dist_to_con_area_id_154',
                'dist_to_con_area_id_155',
                'dist_to_con_area_id_156',
                'dist_to_con_area_id_157',
                'dist_to_con_area_id_158',
                'dist_to_con_area_id_159',
                'dist_to_con_area_id_160',
                'dist_to_con_area_id_161',
                'dist_to_con_area_id_162',
                'dist_to_con_area_id_163',
                'dist_to_con_area_id_164',
                'dist_to_con_area_id_165',
                'dist_to_con_area_id_166',
                'dist_to_con_area_id_167',
                'dist_to_con_area_id_168',
                'dist_to_con_area_id_169',
                'dist_to_con_area_id_170',
                'dist_to_con_area_id_171',
                'dist_to_con_area_id_172',
                'dist_to_con_area_id_173',
                'dist_to_con_area_id_174',
                'dist_to_con_area_id_175',
                'dist_to_con_area_id_176',
                'dist_to_con_area_id_177',
                'dist_to_con_area_id_178',
                'dist_to_con_area_id_179',
                'dist_to_con_area_id_180',
                'dist_to_con_area_id_181',
                'dist_to_con_area_id_182',
                'dist_to_con_area_id_183',
                'dist_to_con_area_id_184',
                'dist_to_con_area_id_185',
                'dist_to_con_area_id_186',
                'dist_to_con_area_id_187',
                'dist_to_con_area_id_188',
                'dist_to_con_area_id_189',
                'dist_to_con_area_id_190',
                'dist_to_con_area_id_191',
                'dist_to_con_area_id_192',
                'dist_to_con_area_id_193',
                'dist_to_con_area_id_194',
                'dist_to_con_area_id_195',
                'dist_to_con_area_id_196',
                'dist_to_con_area_id_197',
                'dist_to_con_area_id_198',
                'dist_to_con_area_id_199',
                'dist_to_con_area_id_200',
                'dist_to_con_area_id_201',
                'dist_to_con_area_id_202',
                'dist_to_con_area_id_203',
                'dist_to_con_area_id_204',
                'dist_to_con_area_id_205',
                'dist_to_con_area_id_206',
                'dist_to_con_area_id_207',
                'dist_to_con_area_id_208',
                'dist_to_con_area_id_209',
                'dist_to_con_area_id_210',
                'dist_to_con_area_id_211',
                'dist_to_con_area_id_212',
                'dist_to_con_area_id_213',
                'dist_to_con_area_id_214',
                'dist_to_con_area_id_215',
                'dist_to_con_area_id_216',
                'dist_to_con_area_id_217',
                'dist_to_con_area_id_218',
                'dist_to_con_area_id_219',
                'dist_to_con_area_id_220',
                'dist_to_con_area_id_221',
                'dist_to_con_area_id_222',
                'dist_to_con_area_id_223',
                'dist_to_con_area_id_224',
                'dist_to_con_area_id_225',
                'dist_to_con_area_id_226',
                'dist_to_con_area_id_227',
                'dist_to_con_area_id_228',
                'dist_to_con_area_id_229',
                'dist_to_con_area_id_230',
                'dist_to_con_area_id_231',
                'dist_to_con_area_id_232',
                'dist_to_con_area_id_233',
                'dist_to_con_area_id_234',
                'dist_to_con_area_id_235',
                'dist_to_con_area_id_236',
                'dist_to_con_area_id_237',
                'dist_to_con_area_id_238',
                'dist_to_con_area_id_239',
                'dist_to_con_area_id_240',
                'dist_to_con_area_id_241',
                'dist_to_con_area_id_242',
                'dist_to_con_area_id_243',
                'dist_to_con_area_id_244',
                'dist_to_con_area_id_245',
                'dist_to_con_area_id_246',
                'dist_to_con_area_id_247',
                'dist_to_con_area_id_248',
                ]
