from utils import download_and_extract
from dump_route_data import dump_route_names, dump_route_numbers
from dump_stop_places import dump_stops
from dump_labeled_dataset import generate_labeled_dataset

print("Important!: This script should not be ran more than once a day to prevent possible consequences from entur due to excessive downloading.\n")

ruter_routes_export_url = "https://storage.googleapis.com/marduk-production/outbound/netex/rb_rut-aggregated-netex.zip"
oslo_export_url = "https://storage.googleapis.com/marduk-production/tiamat/03_Oslo_latest.zip"
akershus_export_url = "https://storage.googleapis.com/marduk-production/tiamat/32_Akershus_latest.zip"

download_and_extract(ruter_routes_export_url, "ruter_routes_export")
download_and_extract(oslo_export_url, "oslo_akershus_stops_export")
download_and_extract(akershus_export_url, "oslo_akershus_stops_export")
dump_route_numbers("ruter_routes_export")
dump_route_names("ruter_routes_export")
dump_stops("oslo_akershus_stops_export")
generate_labeled_dataset()