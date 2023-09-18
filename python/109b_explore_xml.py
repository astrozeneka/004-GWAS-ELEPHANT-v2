import xml.etree.ElementTree as ET


if __name__ == '__main__':
    tree = ET.parse("../data/107c_blast_output_swissprot/hair-sig.xml")
    root = tree.getroot()
    hits = [a for a in root if a.tag == "Hit"]

    # This result should be confirmed with other paper (similar to Deventer et al)
    print()
