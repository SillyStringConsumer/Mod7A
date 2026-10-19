# -*- coding: utf-8 -*-
# PalmerPenguinsM7.py
# Kyler Dulaney
# 10/18/2026
# Process Palmer Penguin data using String operations

import math

# constants representing the species and counts
SP_CHINSTRAP = "Chinstrap"
SP_GENTOO = "Gentoo"
SP_ADELIE = "Adelie"

NUM_CHINSTRAP = 68
NUM_GENTOO = 123
NUM_ADELIE = 151


# instructor-provided function
def read_penguin_row(row_number):
    penguin_row = ""

    # open the CSV file and skip the header row
    with open("PalmerPenguins.csv", "r") as penguin_file:
        penguin_file.readline()

        current_row = 1

        # search for the requested data row
        for row in penguin_file:
            if current_row == row_number:
                penguin_row = row.strip()
                break

            current_row += 1

    # return the requested row as a string
    return penguin_row


# functions for penguin analysis
def calculate_percentage(count, total):
    return count / total * 100


def classify_species(percent):
    if percent < 25:
        return "small"
    elif percent < 40:
        return "medium"
    else:
        return "large"


def get_position_description(selected_species, largest_species, smallest_species):
    if selected_species == largest_species:
        return "largest"
    elif selected_species == smallest_species:
        return "smallest"
    else:
        return "middle-sized"


def display_species_statistics(names, counts, percentages):
    for index, species in enumerate(names):
        print(f"{species}: {counts[index]} ({percentages[index]:.2f}%)")


def display_penguin_observation(sample_number, species, bill_length, bill_depth, body_mass, sex):
    print()
    print("Sample Penguin Observation")
    print(f"{'Sample Number:':<20}{sample_number}")
    print(f"{'Species:':<20}{species}")
    print(f"{'Bill length:':<20}{bill_length} mm")
    print(f"{'Bill depth:':<20}{bill_depth} mm")
    print(f"{'Body mass:':<20}{body_mass} g")
    print(f"{'Sex:':<20}{sex.lower()}")


def main():
    # lists containing related penguin data
    species_names = [
        SP_CHINSTRAP,
        SP_GENTOO,
        SP_ADELIE
    ]

    species_counts = [
        NUM_CHINSTRAP,
        NUM_GENTOO,
        NUM_ADELIE
    ]

    # calculate dataset statistics
    total_species = len(species_names)
    total_penguins = sum(species_counts)

    average_penguins = total_penguins / total_species
    average_penguins_rounded_up = math.ceil(average_penguins)

    chinstrap_percent = calculate_percentage(species_counts[0], total_penguins)
    gentoo_percent = calculate_percentage(species_counts[1], total_penguins)
    adelie_percent = calculate_percentage(species_counts[2], total_penguins)

    # list containing species percentages
    species_percentages = [
        chinstrap_percent,
        gentoo_percent,
        adelie_percent
    ]

    largest_count = max(species_counts)
    smallest_count = min(species_counts)

    largest_index = species_counts.index(largest_count)
    smallest_index = species_counts.index(smallest_count)

    largest_species = species_names[largest_index]
    smallest_species = species_names[smallest_index]

    # output formatted statistics
    print("Introducing the Palmer Penguins:")
    print(f"\t{species_names[0]}!")
    print(f"\t{species_names[1]}!")
    print("and last but not least...")
    print(f"\t{species_names[2]}!")
    print()

    print(f"There are a total of {total_species} penguin species in this dataset.")
    print(f"There are a total of {total_penguins} penguins in the dataset.")
    print(f"The average number of penguins per species is {average_penguins:.1f}.")
    print(f"The average rounded up is {average_penguins_rounded_up} penguins.")

    # display species statistics using a function
    display_species_statistics(
        species_names, species_counts, species_percentages
    )

    print(f"The species with the most observations is {largest_species} with {largest_count} penguins.")
    print(f"The species with the fewest observations is {smallest_species} with {smallest_count} penguins.")

    # retrieve, split, convert, and display two sample penguins
    for row_number in (1, 152):
        penguin_row = read_penguin_row(row_number)
        print()
        print("Sample dataset row:")
        print(penguin_row)

        penguin_data = penguin_row.split(",")
        sample_number = int(penguin_data[0])
        species = penguin_data[1]
        bill_length = float(penguin_data[2])
        bill_depth = float(penguin_data[3])
        body_mass = int(penguin_data[5])
        sex = penguin_data[6]

        display_penguin_observation(
            sample_number, species, bill_length, bill_depth, body_mass, sex
        )

    # initialize the valid selection counter
    valid_selections = 0

    # repeatedly prompt the user to explore species
    print()
    print("Explore a species:")
    species_choice = input("Enter Chinstrap, Gentoo, Adelie, or Done: ")

    while species_choice != "Done":

        # validate the species selection
        if species_choice not in species_names:
            print(f"{species_choice} is not one of the species in this dataset.")
        else:
            # update the number of valid selections
            valid_selections += 1

            # determine the selected species
            if species_choice == species_names[0]:
                selected_index = 0
            elif species_choice == species_names[1]:
                selected_index = 1
            else:
                selected_index = 2

            selected_species = species_names[selected_index]
            selected_count = species_counts[selected_index]
            selected_percent = species_percentages[selected_index]

            # classify the selected species using a function
            size_category = classify_species(selected_percent)

            # determine the species position using a function
            position_description = get_position_description(
                selected_species, largest_species, smallest_species
            )

            # compare the selected count to the average
            average_position = "above" if selected_count > average_penguins else "below"

            # output selected species statistics
            print(f"{selected_species} has {selected_count} observations, representing {selected_percent:.2f}% of the dataset.")
            print(f"{selected_species} is classified as a {size_category} species group.")
            print(f"{selected_species} is the {position_description} species group.")
            print(f"Its observation count is {average_position} the dataset average of {average_penguins:.1f}.")

        # ask for another species
        print()
        species_choice = input("Enter Chinstrap, Gentoo, Adelie, or Done: ")

    # display the exploration summary
    print()
    print(f"You explored {valid_selections} valid species.")
    print("Exploration complete.")


# start the main program
main()
