# load_knowledge.py
# (Legacy compatibility command)
from django.core.management.base import BaseCommand
from app.knowledge_data import UPCYCLING_KNOWLEDGE


class Command(BaseCommand):
    help = "Legacy command: Upcycling knowledge is now baked directly into the lightweight LangChain prompt."

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Clear existing knowledge',
        )

    def handle(self, *args, **options):
        self.stdout.write("=" * 60)
        self.stdout.write("NOTICE: RAG has been replaced with lightweight LangChain.")
        self.stdout.write(f"Domain knowledge ({len(UPCYCLING_KNOWLEDGE)} items) is embedded directly in system prompts.")
        self.stdout.write("No pgvector / local embedding ingestion required. Ready to run!")
        self.stdout.write("=" * 60)
