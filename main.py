import logging
import logging.config
from src.webapp import mainSpider

logging.config.fileConfig('src/common/logging.conf')
logger = logging.getLogger(__name__)



