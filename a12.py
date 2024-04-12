class Paper:
    def __init__(self, ut, year, journal, issn, doi, issue, volume, abstract, title, authors, affiliations, references):
        self.ut = ut
        self.year = year
        self.journal = journal
        self.issn = issn
        self.doi = doi
        self.issue = issue
        self.volume = volume
        self.abstract = abstract
        self.title = title
        self.authors = authors
        self.affiliations = affiliations
        self.references = references

    def from_string(cls, data_string):
        # Assuming data_string is a delimited string of paper details
        details = data_string.split('\t')
        return cls(
            ut=details[0],
            year=details[1],
            journal=details[2],
            issn=details[3],
            doi=details[4],
            issue=details[5],
            volume=details[6],
            abstract=details[7],
            title=details[8],
            authors=details[9],
            affiliations=details[10],
            references=details[11]
        )

    def to_string(self):
        return f"{self.ut}\t{self.year}\t{self.journal}\t{self.issn}\t{self.doi}\t{self.issue}\t{self.volume}\t{self.abstract}\t{self.title}\t{self.authors}\t{self.affiliations}\t{self.references}\n"

    def read_papers(file_path):
        papers = []
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                if line.strip() and not line.startswith('#'):  # Skip headers or empty lines
                    paper = Paper.from_string(line)
                    papers.append(paper)
        return papers

    def write_papers(papers, output_file_path):
        with open(output_file_path, 'w', encoding='utf-8') as file:
            for paper in papers:
                file.write(paper.to_string())

# Usage:
file_path = '作业/path_to_qje2014_2023.txt'
papers = Paper.read_papers(file_path)
output_file_path = '作业/output_papers_details.txt'
Paper.write_papers(papers, output_file_path)
