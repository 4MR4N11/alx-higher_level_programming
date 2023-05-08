#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the head of the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
*/
int check_cycle(listint_t *list)
{
	listint_t *tmp1, *tmp2;

	if (!list || !list->next)
		return (0);
	tmp1 = list;
	tmp2 = list->next;
	while (tmp2 && tmp2->next)
	{
		if (tmp1 == tmp2)
			return (1);
		tmp1 = tmp1->next;
		tmp2 = tmp2->next->next;
	}
	return (0);
}
