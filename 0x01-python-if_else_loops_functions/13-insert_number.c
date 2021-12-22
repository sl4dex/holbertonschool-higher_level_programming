#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - inserts a into a sorted singly linked list
 * @head: head of linked list
 * @number: number element of the linked list
 * Return: address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode, *nxt, *current;

	if (!head)
		return (NULL);
	current = *head;
	while (current)
	{
		if (!(current->next) && current->n < number)
		{
			add_nodeint_end(head, number);
			return (current);
		}
		nxt = current->next;
		if (number <= nxt->n)
		{
			newnode = malloc(sizeof(listint_t));
			if (!newnode)
				return (NULL);
			newnode->n = number;
			current->next = newnode;
			newnode->next = nxt;
			return (newnode);
		}
		else
			current = current->next;
	}
	return (NULL);
}
