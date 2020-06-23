#!/usr/bin/env python3

class StatusRes:
    def __init__(self, status):
        self.status = status
    def is_running(self):
        return self.status == 'running'
    def is_completed(self):
        return self.status == 'completed'

