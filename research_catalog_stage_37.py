# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: ResearchCatalog
import unittest
from research_catalog import ResearchCatalog, Source, Hypothesis, Note, Tag, Conclusion

class TestResearchCatalog(unittest.TestCase):
    def setUp(self):
        self.catalog = ResearchCatalog()

    def test_add_and_retrieve_source(self):
        source = Source(title="Test Source", url="https://example.com", year=2023)
        self.catalog.add_source(source)
        sources = self.catalog.get_sources()
        self.assertEqual(len(sources), 1)
        self.assertEqual(sources[0].title, "Test Source")

    def test_add_and_retrieve_hypothesis(self):
        hyp = Hypothesis(text="AI will replace humans", confidence=0.8)
        self.catalog.add_hypothesis(hyp)
        hypotheses = self.catalog.get_hypotheses()
        self.assertEqual(len(hypotheses), 1)
        self.assertEqual(hypotheses[0].text, "AI will replace humans")

    def test_add_and_retrieve_note(self):
        note = Note(text="Interesting findings", author="Dr. Smith")
        self.catalog.add_note(note)
        notes = self.catalog.get_notes()
        self.assertEqual(len(notes), 1)
        self.assertEqual(notes[0].text, "Interesting findings")

    def test_add_and_retrieve_tag(self):
        tag = Tag(name="ML", category="technology")
        self.catalog.add_tag(tag)
        tags = self.catalog.get_tags()
        self.assertEqual(len(tags), 1)
        self.assertEqual(tags[0].name, "ML")

    def test_add_and_retrieve_conclusion(self):
        conc = Conclusion(text="Research successful", confidence=0.95)
        self.catalog.add_conclusion(conc)
        conclusions = self.catalog.get_conclusions()
        self.assertEqual(len(conclusions), 1)
        self.assertEqual(conclusions[0].text, "Research successful")

    def test_multiple_sources(self):
        self.catalog.add_source(Source(title="Source A", url="https://a.com"))
        self.catalog.add_source(Source(title="Source B", url="https://b.com"))
        sources = self.catalog.get_sources()
        self.assertEqual(len(sources), 2)

    def test_multiple_hypotheses(self):
        self.catalog.add_hypothesis(Hypothesis(text="H1", confidence=0.7))
        self.catalog.add_hypothesis(Hypothesis(text="H2", confidence=0.6))
        hypotheses = self.catalog.get_hypotheses()
        self.assertEqual(len(hypotheses), 2)

    def test_multiple_notes(self):
        self.catalog.add_note(Note(text="N1", author="A"))
        self.catalog.add_note(Note(text="N2", author="B"))
        notes = self.catalog.get_notes()
        self.assertEqual(len(notes), 2)

    def test_multiple_tags(self):
        self.catalog.add_tag(Tag(name="T1", category="cat1"))
        self.catalog.add_tag(Tag(name="T2", category="cat2"))
        tags = self.catalog.get_tags()
        self.assertEqual(len(tags), 2)

    def test_multiple_conclusions(self):
        self.catalog.add_conclusion(Conclusion(text="C1", confidence=0.8))
        self.catalog.add_conclusion(Conclusion(text="C2", confidence=0.9))
        conclusions = self.catalog.get_conclusions()
        self.assertEqual(len(conclusions), 2)

    def test_empty_catalog(self):
        self.assertEqual(len(self.catalog.get_sources()), 0)
        self.assertEqual(len(self.catalog.get_hypotheses()), 0)
        self.assertEqual(len(self.catalog.get_notes()), 0)
        self.assertEqual(len(self.catalog.get_tags()), 0)
        self.assertEqual(len(self.catalog.get_conclusions()), 0)

if __name__ == '__main__':
    unittest.main()
