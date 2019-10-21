# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GpcrdbItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    unipro = scrapy.Field()
    unipro_url = scrapy.Field()
    iupha = scrapy.Field()
    iupha_url = scrapy.Field()
    g_class = scrapy.Field()
    species = scrapy.Field()
    pdb = scrapy.Field()
    pdb_url = scrapy.Field()
    refined_structure = scrapy.Field()
    refined_structure_url = scrapy.Field()
    resolution = scrapy.Field()
    pre_cha = scrapy.Field()
    state = scrapy.Field()
    distance = scrapy.Field()
    g_protei = scrapy.Field()
    arrestin = scrapy.Field()
    fusion = scrapy.Field()
    antibody = scrapy.Field()
    endo_ligand = scrapy.Field()
    ligand_type = scrapy.Field()
    structure_ligand = scrapy.Field()
    structure_lig_function = scrapy.Field()
    structure_lig_type = scrapy.Field()
    method = scrapy.Field()
    sodium_ion_site_choice1 = scrapy.Field()
    sodium_ion_site_choice2 = scrapy.Field()
    senior_author = scrapy.Field()
    reference = scrapy.Field()
    pdb_date = scrapy.Field()
    annotated = scrapy.Field()
    pass
