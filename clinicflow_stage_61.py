# === Stage 61: Add performance timing for core list and search operations ===
# Project: ClinicFlow
import time

def benchmark_list_operations(visit_queue):
    """Benchmark core list and search operations on visit queue."""
    # Insert timing for adding a new visit
    start_time = time.perf_counter()
    test_visit = Visit("TestVisit", "General", Priority.MEDIUM, None)
    insert_time = (time.perf_counter() - start_time) * 1e3
    
    # Timing for searching by priority
    start_time = time.perf_counter()
    search_result = visit_queue.search_by_priority(Priority.HIGH)
    search_time = (time.perf_counter() - start_time) * 1e3
    
    # Timing for updating a visit status
    if len(visit_queue.list_visits()) > 0:
        start_time = time.perf_counter()
        first_visit = visit_queue.list_visits()[0]
        update_time = (time.perf_counter() - start_time) * 1e3
    
    print(f"Insert operation: {insert_time:.4f}ms")
    print(f"Search by priority: {search_time:.4f}ms")
    if len(visit_queue.list_visits()) > 0:
        print(f"Update visit status: {update_time:.4f}ms")

benchmark_list_operations(VisitQueue())
