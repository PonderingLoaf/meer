import pygame, sys, json, math, time, gui, assetParser as assets, units; from enum import Enum

class StateMachine(Enum):
    menu = 0
    map = 1
    play = 2
    loading = 3