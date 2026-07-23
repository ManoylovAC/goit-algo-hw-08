import heapq


def min_cost_to_connect_cables(cables: list[int]) -> int:
    """
    Return the minimum total cost of connecting all cables.
    """

    # Convert the list into a min-heap.
    heap = cables[:]
    heapq.heapify(heap)

    total_cost = 0

    while len(heap) > 1:
        # Connect the two shortest cables.
        min_val_1 = heapq.heappop(heap)
        min_val_2 = heapq.heappop(heap)
        merged_val = min_val_1 + min_val_2

        total_cost += merged_val
        heapq.heappush(heap, merged_val)
        # print(
        #     f"{min_val_1:>2} + {min_val_2:>2} = {merged_val:>2}"
        #     " | "
        #     f"total: {total_cost}"
        # )

    return total_cost


if __name__ == "__main__":
    cables = [4, 7, 5, 12, 3, 15]

    print("Cable lengths:", cables)
    print("Minimum cost to connect all cables:", min_cost_to_connect_cables(cables))
