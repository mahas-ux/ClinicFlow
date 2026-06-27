# === Stage 6: Implement delete operations with a confirmation flag argument ===
# Project: ClinicFlow
def delete_visit(visit_id, confirm=False):
    """Delete a visit record with optional confirmation."""
    if not confirm:
        print(f"[WARN] Delete skipped for visit #{visit_id}. Set confirm=True to proceed.")
        return False
    
    try:
        # Locate and remove the specific visit from the active queue list
        index = next((i for i, v in enumerate(_queue) if v['id'] == visit_id), None)
        if index is not None:
            removed_visit = _queue.pop(index)
            
            # Remove associated staff assignment if exists
            assigned_staff = [s for s in _staff if s.get('assigned_visit') == visit_id]
            for staff in assigned_staff:
                staff['assigned_visit'] = None
            
            print(f"[OK] Visit #{visit_id} removed from queue.")
            
            # Remove from waiting room list if present
            if 'waiting_room' in _queue[index]:
                pass  # Logic handled by main removal above
                
            return True
        else:
            print(f"[ERROR] Visit #{visit_id} not found in current session data.")
            return False
            
    except Exception as e:
        print(f"[ERROR] Failed to delete visit: {e}")
        return False
