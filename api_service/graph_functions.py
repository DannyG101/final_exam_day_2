import io
import matplotlib.pyplot as plt


def create_line_graph(results):
    lon = []
    lat = []
    for result in results:
        lon.append(result[0])
        lat.append(result[1])

    fig = plt.figure()
    plt.plot(lon, lat, marker='o')
    plt.title("entity_id")
    plt.xlabel('lon')
    plt.ylabel("lat")
    img_buf = io.BytesIO()
    plt.savefig(img_buf, format='png')
    plt.close(fig)
    return img_buf