# -*- coding: utf-8 -*-
import scrapy

from gpcrdb.items import GpcrdbItem


class GpcrdbStructureSpider(scrapy.Spider):
    name = 'structure'
    allowed_domains = ['https://www.gpcrdb.org/']
    start_urls = ['https://www.gpcrdb.org/structure//']

    def parse(self, response):
        structures = response.css('#structures_scrollable tbody tr')
        i = 1
        for structure in structures:
            print(i)
            i += 1
            item = GpcrdbItem()

            unipro = structure.css('td:nth-child(2) span a::text').extract_first()
            unipro_url = structure.css('td:nth-child(2) span a::attr(href)').extract_first()

            iupha = structure.css('td:nth-child(3) span a::text').extract_first()
            iupha_url = structure.css('td:nth-child(3) span a::attr(href)').extract_first()[1:]

            g_class = structure.css('td:nth-child(5) span::text').extract_first().strip()
            species = structure.css('td:nth-child(6)::text').extract_first().strip()

            pdb = structure.css('td:nth-child(7) a::text').extract_first()
            pdb_url = structure.css('td:nth-child(7) a::attr(href)').extract_first()

            refined_structure = structure.css('td:nth-child(8) a::text').extract_first()
            refined_structure_url = structure.css('td:nth-child(8) a::attr(href)').extract_first()

            resolution = structure.css('td:nth-child(9)::text').extract_first()
            pre_cha = structure.css('td:nth-child(10)::text').extract_first()
            state = structure.css('td:nth-child(11)::text').extract_first()
            distance = structure.css('td:nth-child(12)::text').extract_first()
            g_protei = structure.css('td:nth-child(13)::text').extract_first().strip()
            arrestin = structure.css('td:nth-child(14)::text').extract_first().strip()
            fusion = structure.css('td:nth-child(15)::text').extract_first().strip()
            antibody = structure.css('td:nth-child(16)::text').extract_first().strip()
            endo_ligand = structure.css('td:nth-child(17)::text').extract_first().strip()
            ligand_type = structure.css('td:nth-child(18)::text').extract_first()

            tmp_ligands = structure.css('td:nth-child(19)::text').extract()
            results = []
            for ligand in tmp_ligands:
                results.append(ligand.strip())
            structure_ligands = results

            structure_lig_function = structure.css('td:nth-child(20)::text').extract_first().strip()
            structure_lig_type = structure.css('td:nth-child(21)::text').extract_first().strip()
            method = structure.css('td:nth-child(22)::text').extract_first().strip()
            sodium_ion_site_choice1 = structure.css('td:nth-child(23)::text').extract_first().strip()
            sodium_ion_site_choice2 = structure.css('td:nth-child(24)::text').extract_first().strip()
            senior_author = structure.css('td:nth-child(25)::text').extract_first().strip()
            reference = structure.css('td:nth-child(26) a::attr(href)').extract_first().strip()
            pdb_date = structure.css('td:nth-child(27)::text').extract_first().strip()
            annotated = structure.css('td:nth-child(28)::text').extract_first().strip()

            item["unipro"] = unipro
            item["unipro_url"] = unipro_url
            item["iupha"] = iupha
            item["iupha_url"] = iupha_url
            item["g_class"] = g_class
            item["species"] = species
            item["pdb"] = pdb
            item["pdb_url"] = pdb_url
            item["refined_structure"] = refined_structure
            item["refined_structure_url"] = refined_structure_url
            item["resolution"] = resolution
            item["pre_cha"] = pre_cha
            item["state"] = state
            item["distance"] = distance
            item["g_protei"] = g_protei
            item["arrestin"] = arrestin
            item["fusion"] = fusion
            item["antibody"] = antibody
            item["endo_ligand"] = endo_ligand
            item["ligand_type"] = ligand_type
            item["structure_ligand"] = structure_ligands
            item["structure_lig_function"] = structure_lig_function
            item["structure_lig_type"] = structure_lig_type
            item["method"] = method
            item["sodium_ion_site_choice1"] = sodium_ion_site_choice1
            item["sodium_ion_site_choice2"] = sodium_ion_site_choice2
            item["senior_author"] = senior_author
            item["reference"] = reference
            item["pdb_date"] = pdb_date
            item["annotated"] = annotated

            yield item
