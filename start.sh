#!/bin/bash
docker run -v $(pwd)/csv_data:/app/csv_data ip_gathering_app:latest
