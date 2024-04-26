
import sys
from stagesController import StagesController

def main()->int:
    stagesController = StagesController()
    stagesController.controller()

if __name__ == '__main__':
    sys.exit(main())
