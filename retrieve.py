def search_similar_products(query, store):
    q_embed = store["embeddings"][0]  # Simplified for demo
    D, I = store["index"].search(np.array([q_embed]), k=5)
    return [store["docs"][i] for i in I[0]]