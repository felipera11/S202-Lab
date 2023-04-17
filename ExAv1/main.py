from database import Database
from MotoristaDAO import MotoristaDAO
from MotoristaCLI import MotoristaCLI

db = Database(database="ExAv1", collection="Motorista")
motoristaDAO = MotoristaDAO(database=db)

motoristaCLI = MotoristaCLI(motoristaDAO)
motoristaCLI.run()