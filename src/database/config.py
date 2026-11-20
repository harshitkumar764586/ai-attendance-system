import streamlit as st


from supabase import create_client, Client

class _SupabaseProxy:
    @property
    def _client(self) -> Client:
        return create_client(
            st.secrets["SUPABASE_URL"],
            st.secrets["SUPABASE_KEY"]
        )
    def __getattr__(self, name):
        return getattr(self._client, name)

supabase = _SupabaseProxy()