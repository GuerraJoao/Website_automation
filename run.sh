#!/bin/bash
behave --junit --junit-directory reports/$(date +%s)
