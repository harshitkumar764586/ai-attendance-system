import streamlit as st
from supabase import create_client
import pandas as pd
import toml
import os

# Load credentials from .streamlit/secrets.toml
secrets_path = os.path.join(".streamlit", "secrets.toml")
if os.path.exists(secrets_path):
    secrets = toml.load(secrets_path)
    url = secrets.get("SUPABASE_URL")
    key = secrets.get("SUPABASE_KEY")
else:
    url = "https://pjqvugqmowzerskcmbmt.supabase.co"
    key = "sb_publishable_RApPXJGoJmRmBIcfqDWT6g_xMp1kUUS"

supabase = create_client(url, key)

tables = ["teachers", "students", "subjects", "subject_students", "attendance_logs"]

print("=" * 60)
print("           SNAPCLASS DATABASE VIEWER")
print("=" * 60)

for table_name in tables:
    try:
        response = supabase.table(table_name).select("*").execute()
        data = response.data
        print(f"\n📁 TABLE: {table_name.upper()} ({len(data)} total records)")
        print("-" * 60)
        
        if not data:
            print("  (Empty - no records yet)")
        else:
            # Clean up heavy embeddings for clean terminal display
            display_data = []
            for row in data:
                clean_row = dict(row)
                if "face_embedding" in clean_row and clean_row["face_embedding"]:
                    clean_row["face_embedding"] = f"✅ 128-d vector"
                if "voice_embedding" in clean_row and clean_row["voice_embedding"]:
                    clean_row["voice_embedding"] = f"✅ Audio vector"
                if "password" in clean_row:
                    clean_row["password"] = clean_row["password"][:15] + "..."
                display_data.append(clean_row)
            
            df = pd.DataFrame(display_data)
            print(df.to_string(index=False))
        print("=" * 60)
    except Exception as e:
        print(f"Error fetching {table_name}: {e}")
