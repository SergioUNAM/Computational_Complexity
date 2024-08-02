import time
import random
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt


def main():
    # Create XML structure
    plot = ET.Element('Plot', title="Average List Element Access Time")
    axes = ET.SubElement(plot, 'Axes')
    ET.SubElement(axes, 'XAxis', min="1000", max="200000").text = "List Size"

    # Create XML tree and write to file
    tree = ET.ElementTree(plot)
    tree.write("ListAccessTiming.xml", encoding="UTF-8", xml_declaration=True)

    # Test lists of size 1000 to 200000.
    xmin = 1000
    xmax = 200000

    # Lists to store sizes and access times
    xList = []
    yList = []

    for x in range(xmin, xmax + 1, 1000):
        xList.append(x)
        prod = 0

        # Create a list of size x with all 0's
        lst = [0] * x

        # Let any garbage collection/memory allocation complete
        time.sleep(1)

        # Time before the 1000 test retrievals
        starttime = time.perf_counter()

        for _ in range(1000):
            # Find a random location within the list and retrieve a value.
            index = random.randint(0, x - 1)
            val = lst[index]
            prod = prod * val

        # Time after the 1000 test retrievals
        endtime = time.perf_counter()

        # The difference in time between start and end.
        delaT = endtime - starttime

        # Divide by 1000 for the average access time (in microseconds).
        accessTime = delaT * 1_000_000
        yList.append(accessTime)

    # Append average access time data to XML
    sequence = ET.SubElement(plot, 'Sequence', title="Average Access Time vs List Size", color="red")
    for i in range(len(xList)):
        ET.SubElement(sequence, 'DataPoint', x=str(xList[i]), y=str(yList[i]))

    # Test access at 100 random locations within a list of 200,000 elements
    lst = [0] * 200000
    xList = list(range(200000))
    yList = [0] * 200000

    time.sleep(2)

    for _ in range(100):
        starttime = time.perf_counter()
        index = random.randint(0, 199999)
        lst[index] += 1
        endtime = time.perf_counter()
        delaT = endtime - starttime
        yList[index] += int(delaT * 1_000_000)

    # Append access time distribution data to XML
    sequence = ET.SubElement(plot, 'Sequence', title="Access Time Distribution", color="blue")
    for i in range(len(xList)):
        if lst[i] > 0:
            ET.SubElement(sequence, 'DataPoint', x=str(i), y=str(yList[i] / lst[i]))

    # Write the updated XML tree to file
    tree.write("ListAccessTiming.xml", encoding="UTF-8", xml_declaration=True)



def plot_from_xml(file_path):
    # Parse the XML file
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Variables to hold the data for different sequences
    sequences = []

    # Iterate over the sequences in the XML file
    for sequence in root.findall('Sequence'):
        title = sequence.get('title')
        color = sequence.get('color')

        x_data = []
        y_data = []

        # Iterate over DataPoints in the sequence
        for datapoint in sequence.findall('DataPoint'):
            x = datapoint.get('x')
            y = datapoint.get('y')

            # Only add points if x and y are not None
            if x is not None and y is not None:
                try:
                    x_data.append(float(x))
                    y_data.append(float(y))
                except ValueError:
                    # Handle the case where conversion to float fails
                    print(f"Warning: Could not convert {x}, {y} to float. Skipping these data points.")
                    continue

        sequences.append((title, x_data, y_data, color))

    # Plot the data
    plt.figure(figsize=(10, 6))
    for title, x_data, y_data, color in sequences:
        plt.plot(x_data, y_data, label=title, color=color)

    # Set plot labels and title
    plt.xlabel('List Size or Index')
    plt.ylabel('Average Access Time (μs)')
    plt.title('List Access Timing Analysis')
    plt.legend()
    plt.grid(True)
    plt.show()

# Example usage
plot_from_xml("ListAccessTiming.xml")


if __name__ == "__main__":
    main()