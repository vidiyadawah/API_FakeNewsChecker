import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class Visualize: #gotta redo this part 
    @staticmethod
    def plot_sources(data):
        source_counts = {}
        for item in data:
            source = item['source']
            source_counts[source] = source_counts.get(source, 0) + 1

        sources = list(source_counts.keys())
        counts = list(source_counts.values())

        plt.figure(figsize=(10, 6))
        sns.barplot(x=counts, y=sources)
        plt.title('News Source Distribution')
        plt.xlabel('Number of Articles')
        plt.ylabel('Sources')
        plt.show()

    @staticmethod
    def plot_fact_checks(data):
        fact_check_counts = {'True': 0, 'False': 0}
        for item in data:
            if item['fact_checks']:
                for check in item['fact_checks']:
                    if check.get('textualRating', '').lower() in ['true', 'mostly true']:
                        fact_check_counts['True'] += 1
                    else:
                        fact_check_counts['False'] += 1

        labels = list(fact_check_counts.keys())
        counts = list(fact_check_counts.values())

        plt.figure(figsize=(8, 8))
        plt.pie(counts, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title('Fact-Check Results')
        plt.show()
