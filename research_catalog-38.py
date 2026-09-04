# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: ResearchCatalog
import unittest
from research_catalog import ResearchCatalog, Research, Source, Tag, Hypothesis, Note, Conclusion

class TestEdgeCases(unittest.TestCase):
    def test_empty_catalog(self):
        catalog = ResearchCatalog()
        self.assertEqual(catalog.researches, [])
        with self.assertRaises(ValueError):
            catalog.add_research("title")

    def test_duplicate_research(self):
        catalog = ResearchCatalog()
        r1 = Research("r1", "title1", "desc1")
        r2 = Research("r1", "title2", "desc2")
        catalog.add_research(r1)
        with self.assertRaises(ValueError):
            catalog.add_research(r2)

    def test_research_with_all_fields(self):
        r = Research("r1", "title", "desc", "source", ["t1", "t2"], "h1", "n1", "c1")
        self.assertEqual(r.title, "title")
        self.assertEqual(r.source, "source")
        self.assertEqual(r.tags, ["t1", "t2"])
        self.assertEqual(r.hypothesis, "h1")
        self.assertEqual(r.note, "n1")
        self.assertEqual(r.conclusion, "c1")

    def test_research_without_optional_fields(self):
        r = Research("r1", "title", "desc")
        self.assertIsNone(r.source)
        self.assertEqual(r.tags, [])
        self.assertIsNone(r.hypothesis)
        self.assertIsNone(r.note)
        self.assertIsNone(r.conclusion)

    def test_search_by_title(self):
        catalog = ResearchCatalog()
        catalog.add_research(Research("r1", "AI", "desc1"))
        catalog.add_research(Research("r2", "ML", "desc2"))
        results = catalog.search("AI")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "AI")

    def test_search_by_tag(self):
        catalog = ResearchCatalog()
        catalog.add_research(Research("r1", "title1", "desc1", tags=["ML", "DL"]))
        catalog.add_research(Research("r2", "title2", "desc2", tags=["DL", "NLP"]))
        results = catalog.search(tags=["DL"])
        self.assertEqual(len(results), 2)

    def test_search_by_source(self):
        catalog = ResearchCatalog()
        catalog.add_research(Research("r1", "title1", "desc1", source="arxiv"))
        catalog.add_research(Research("r2", "title2", "desc2", source="google"))
        results = catalog.search(source="arxiv")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "title1")

    def test_search_by_conclusion(self):
        catalog = ResearchCatalog()
        catalog.add_research(Research("r1", "title1", "desc1", conclusion="positive"))
        catalog.add_research(Research("r2", "title2", "desc2", conclusion="negative"))
        results = catalog.search(conclusion="positive")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "title1")

    def test_search_empty(self):
        catalog = ResearchCatalog()
        results = catalog.search("nonexistent")
        self.assertEqual(len(results), 0)

    def test_search_invalid(self):
        catalog = ResearchCatalog()
        with self.assertRaises(ValueError):
            catalog.search("invalid_search")

    def test_research_with_empty_tags(self):
        r = Research("r1", "title", "desc", tags=[])
        self.assertEqual(r.tags, [])

    def test_research_with_none_fields(self):
        r = Research("r1", "title", "desc", source=None, tags=None, hypothesis=None, note=None, conclusion=None)
        self.assertEqual(r.source, None)
        self.assertEqual(r.tags, [])
        self.assertEqual(r.hypothesis, None)
        self.assertEqual(r.note, None)
        self.assertEqual(r.conclusion, None)

    def test_research_with_special_characters(self):
        r = Research("r1", "title with !@#$%^&*() characters", "description with émojis 🎉 and unicode ∑")
        self.assertEqual(r.title, "title with !@#$%^&*() characters")
        self.assertEqual(r.description, "description with émojis 🎉 and unicode ∑")

    def test_research_with_unicode_source(self):
        r = Research("r1", "title", "desc", source="arXiv:2201.00000")
        self.assertEqual(r.source, "arXiv:2201.00000")

    def test_research_with_long_title(self):
        long_title = "A" * 100
        r = Research("r1", long_title, "desc")
        self.assertEqual(len(r.title), 100)
